CWE_ID = "CWE-434"
CVE_ID = "CVE-2020-25213"
IP_ADDR = ""
PORT_NO = "8082"

IMAGE_NAME    = "ridgesecuritydocker/cve-2020-25213:mywordpress1"
IMAGE_SRC     = "https://hub.docker.com/r/ridgesecuritydocker/cve-2020-25213"
IMAGE_RUN_CMD = "sudo docker run -it -p 8080:80 -d ridgesecuritydocker/cve-2020-25213:mywordpress1"

MAIN_ATTACK_PATH = "~/TEST_ATTACKS/ATTACK_YAMLS/CWE-434_Unrestricted-Upload-of-File/CVE-2020-25213_Payload.yaml"
MAIN_YAML_AUTHOR = "~/nuclei-templates/cves/2020/CVE-2020-25213.yaml (Original) is rewritten by SAID, referencing the MAIN_YAML_SOURCE"
MAIN_YAML_SOURCE = "https://infosecwriteups.com/exploiting-cve-2020-25213-wp-file-manager-wordpress-plugin-6-9-3f79241f0cd8"
