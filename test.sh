#repo_version=$(cd ../projetos/dev/bot-demo-with-ci-cd && git describe --tag)
repo_version="1.0"
if java -jar botCLI.jar bot list --bid=botDemoCiCd | grep "Version: $repo_version" || [[ $? -eq 0 ]]; then
  echo "Versão encontrada: $repo_version"
  echo "DEPLOYED=1"
else
  echo "Versão encontrada: $repo_version"
  echo "DEPLOYED=0"
fi
