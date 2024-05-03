# Onboarding Neurotech

Projeto de onboarding da neurotech

## Dependências

- Python 3.12.3
- pip 24.0

## Como rodar

### Criando um ambiente virtual

- Windows
  Considerando o uso de [pyenv-win](https://github.com/pyenv-win/pyenv-win) no projeto, para criar um ambiente virtual, basta rodar o comando:

```shell
.\virtualenv.ps1 $VIRTUAL_ENV_NAME$
```

- Linux
  Considerando o uso de [pyenv](https://github.com/pyenv/pyenv) no projeto, para criar um ambiente virtual, basta rodar o comando:

```bash
./virtualenv.sh $VIRTUAL_ENV_NAME$
```

Após isso, rode o comando abaixo para executar o programa:

```bash
cd src/
python main.py NF_CODE(Optional)
```

## Testes

Com o ambiente virtual ativado, rode:

```bash
cd src/
python test.py
```
