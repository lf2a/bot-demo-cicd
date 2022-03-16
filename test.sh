#repo_version=$(cd ../projetos/dev/bot-demo-with-ci-cd/ && git describe --tags $(git rev-list --tags --max-count=1))
repo_version="1.0"
#if java -jar botCLI.jar bot list --bid=botDemoCiCd | grep "Version: $repo_version" || [[ $? -eq 0 ]]; then
#  echo "Versão encontrada: $repo_version"
#  echo "DEPLOYED=1"
#else
#  echo "Versão encontrada: $repo_version"
#  echo "DEPLOYED=0"
#fi

if $repo_version && [[ $? -ne 0 ]]; then
  echo "nao passa"
else
#  repo_version=$(git describe --tags $(git rev-list --tags --max-count=1) || if [[ $? -eq 0 ]]; then exit 0; fi)
  if java -jar botCLI.jar bot list --bid=botDemoCiCd | grep "Version: $repo_version" || [[ $? -eq 0 ]]; then
    echo "Já foi feito deploy"
    echo $repo_version
  else
    echo "Fazer deploy"
  fi
fi
