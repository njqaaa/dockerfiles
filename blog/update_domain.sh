#!/bin/bash
domain=$1
config_file='/root/blog/_config.yml'
config_file_bak='/root/blog/_config.yml-bak'
if [[ ! -f ${config_file_bak} ]];then
    cp ${config_file} ${config_file_bak}
else
    cp ${config_file_bak} ${config_file}
fi

if [[ ! -z ${domain} ]];then
    echo "domain is ${domain}"
    sed -i 's/yoursite.com/'${domain}'/g' ${config_file}
else 
    echo "domain is 127.0.0.1"
    sed -i 's/yoursite.com/'127.0.0.1'/g' ${config_file}
fi

#重启
kill -HUP 1
