java -jar botCLI.jar bot list --bid=botDemoCiCd | grep "Version: 1.0+672ba421"

if [[ $? -eq 0 ]]; then
  echo "achou"
else
  echo "nao achou"
fi
