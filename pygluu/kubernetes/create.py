"""
 License terms and conditions for Gluu Cloud Native Edition:
 https://www.apache.org/licenses/LICENSE-2.0
 Installs Gluu
"""
import argparse
import sys
from pygluu.kubernetes.couchbase import Couchbase
from pygluu.kubernetes.terminal.prompt import Prompt
from pygluu.kubernetes.helpers import get_logger, copy_templates
from pygluu.kubernetes.gluu import Gluu
from pygluu.kubernetes.settings import ValuesHandler

logger = get_logger("gluu-create        ")


def create_parser():
    """Create parser to handle arguments from CLI.
    :return:
    """
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(title="Commands", dest="subparser_name")
    subparsers.add_parser("generate-settings", help="Generate settings.json to install "
                                                    "Gluu Cloud Native Edition non-interactively")
    subparsers.add_parser("install-ldap-backup", help="Install ldap backup cronjob only.")
    subparsers.add_parser("restore", help="Install Gluu Cloud Native Edition with a "
                                          "running database and previous configuration")
    subparsers.add_parser("upgrade", help="Upgrade Gluu Cloud Native Edition")
    subparsers.add_parser("upgrade-values-yaml", help="Upgrade Gluu Cloud Native Edition")
    subparsers.add_parser("install-couchbase", help="Install Couchbase only. Used with installation of Gluu with Helm")
    subparsers.add_parser("install-couchbase-backup", help="Install Couchbase backup only.")
    subparsers.add_parser("uninstall-couchbase", help="Uninstall Couchbase only.")
    subparsers.add_parser("install", help="Install Gluu Cloud Native Edition using helm. "
                                          "This also installs the nginx-ingress chart")
    subparsers.add_parser("uninstall", help="Uninstall Gluu Cloud Native Edition using helm. "
                                            "This also uninstalls the nginx-ingress chart")
    subparsers.add_parser("install-gg-dbmode", help="Install Gluu Gateway with Postgres database using helm")
    subparsers.add_parser("uninstall-gg-dbmode", help="Install Gluu Gateway with Postgres database using helm")

    subparsers.add_parser("install-gluu", help="Install Gluu Cloud Native Edition using helm. "
                                               "This assumes nginx-ingress is installed")
    subparsers.add_parser("uninstall-gluu", help="Uninstall Gluu Cloud Native Edition using helm."
                                                 "This only uninstalls Gluu")
    subparsers.add_parser("version", help="Outputs version of pygluu installer.")
    return parser


def main():
    parser = create_parser()
    args = parser.parse_args(sys.argv[1:])

    if not args.subparser_name:
        parser.print_help()
        return

    if args.subparser_name == "version":
        from pygluu.kubernetes import __version__
        logger.info(f"pygluu installer version is : {__version__}")
        return

    copy_templates()
    settings = ValuesHandler()
    # settings.validate()
    # if not settings.validate():
    #     for error in settings.errors:
    #         logger.error(error)
    #     sys.exit()

    prompts = Prompt()
    prompts.prompt()
    settings = ValuesHandler()

    try:
        if args.subparser_name == "install-ldap-backup":
            gluu = Gluu()
            gluu.install_ldap_backup()

        elif args.subparser_name == "uninstall-gluu":
            from pygluu.kubernetes.terminal.helm import PromptHelm
            prompt_helm = PromptHelm(settings)
            prompt_helm.prompt_helm()
            gluu = Gluu()
            gluu.uninstall_gluu()
            if settings.get("installer-settings.redis.install"):
                # TODO: Make sure remove redis or postgres if installled by Gluu
                logger.info("remove me after implementing TODO")
        elif args.subparser_name == "upgrade-values-yaml":
            from pygluu.kubernetes.terminal.upgrade import PromptUpgrade
            # New feature in 4.2 compared to 4.1 and hence if enabled should make sure postgres is installed.
            gluu = Gluu()
            if settings.get("installer-settings.jackrabbit.clusterMode") and \
                    settings.get("installer-settings.postgres.install"):
                # TODO: Make sure postgres is installed
                logger.info("remove me after implementing TODO")
            prompt_upgrade = PromptUpgrade(settings)
            prompt_upgrade.prompt_upgrade()
            logger.info("Patching values.yaml for helm upgrade...")
            logger.info("Please find your patched values.yaml at the location ./helm/gluu/values.yaml."
                        "Continue with the steps found at https://gluu.org/docs/gluu-server/latest/upgrade/#helm")

        elif args.subparser_name == "install-couchbase":
            from pygluu.kubernetes.terminal.couchbase import PromptCouchbase
            prompt_couchbase = PromptCouchbase(settings)
            prompt_couchbase.prompt_couchbase()
            couchbase = Couchbase()
            couchbase.install()

        elif args.subparser_name == "install-couchbase-backup":
            from pygluu.kubernetes.terminal.couchbase import PromptCouchbase
            prompt_couchbase = PromptCouchbase(settings)
            prompt_couchbase.prompt_couchbase()
            couchbase = Couchbase()
            couchbase.setup_backup_couchbase()

        elif args.subparser_name == "uninstall-couchbase":
            from pygluu.kubernetes.terminal.couchbase import PromptCouchbase
            prompt_couchbase = PromptCouchbase(settings)
            prompt_couchbase.prompt_couchbase()
            couchbase = Couchbase()
            couchbase.uninstall()

        elif args.subparser_name == "generate-settings":
            logger.info("settings.json has been generated")

        elif args.subparser_name == "install":
            from pygluu.kubernetes.terminal.helm import PromptHelm
            prompt_helm = PromptHelm(settings)
            prompt_helm.prompt_helm()
            gluu = Gluu()
            if settings.get("installer-settings.jackrabbit.clusterMode"):
                from pygluu.kubernetes.postgres import Postgres
                postgres = Postgres()
                postgres.install_postgres()
            if settings.get("installer-settings.redis.install"):
                from pygluu.kubernetes.redis import Redis
                redis = Redis()
                redis.uninstall_redis()
                redis.install_redis()
            gluu.install_gluu()

        elif args.subparser_name == "uninstall":
            from pygluu.kubernetes.terminal.helm import PromptHelm
            from pygluu.kubernetes.gluugateway import GluuGateway
            prompt_helm = PromptHelm(settings)
            prompt_helm.prompt_helm()
            gluu = Gluu()
            gluugateway = GluuGateway()
            gluu.uninstall_gluu()
            gluu.uninstall_nginx_ingress()
            gluugateway.uninstall_gluu_gateway_dbmode()
            gluugateway.uninstall_gluu_gateway_ui()
            logger.info("Please wait...")

        elif args.subparser_name == "install-gluu":
            from pygluu.kubernetes.terminal.helm import PromptHelm
            prompt_helm = PromptHelm(settings)
            prompt_helm.prompt_helm()
            gluu = Gluu()
            gluu.uninstall_gluu()
            gluu.install_gluu(install_ingress=False)

        elif args.subparser_name == "install-gg-dbmode":
            from pygluu.kubernetes.terminal.helm import PromptHelm
            from pygluu.kubernetes.postgres import Postgres
            from pygluu.kubernetes.gluugateway import GluuGateway
            prompt_helm = PromptHelm(settings)
            prompt_helm.prompt_helm()
            postgres = Postgres()
            postgres.patch_or_install_postgres()
            gluugateway = GluuGateway()
            gluugateway.install_gluu_gateway_dbmode()
            gluugateway.install_gluu_gateway_ui()

        elif args.subparser_name == "uninstall-gg-dbmode":
            from pygluu.kubernetes.terminal.helm import PromptHelm
            from pygluu.kubernetes.postgres import Postgres
            from pygluu.kubernetes.gluugateway import GluuGateway
            prompt_helm = PromptHelm(settings)
            prompt_helm.prompt_helm()
            postgres = Postgres()
            postgres.uninstall_postgres()
            gluugateway = GluuGateway()
            gluugateway.uninstall_gluu_gateway_dbmode()
            gluugateway.uninstall_gluu_gateway_ui()

    except KeyboardInterrupt:
        print("\n[I] Canceled by user; exiting ...")


if __name__ == "__main__":
    main()
