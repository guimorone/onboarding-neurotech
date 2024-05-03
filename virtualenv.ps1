Param(
  [string]$name
)

if ($PSBoundParameters.ContainsKey('name')) {
  pyenv update
  pyenv install 3.12.3
  pyenv local 3.12.3
  pyenv exec python -m pip install virtualenv
  pyenv exec python -m venv $name
  .\.venv\Scripts\activate
  pip install -r requirements.txt
}
else {
  Write-Host 'No arguments were passed for "name"'
}

