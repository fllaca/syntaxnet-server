# Syntaxne server

## Build

```
docker build -t fllaca/syntaxnet-server .
```

## Run

```
docker run --name parseface -v $(pwd)/../syntaxnet-lang-models:/fer --rm -i -t fllaca/syntaxnet-server
```

## Usage

```shell
curl -s -X POST -d '{ "text": "alarma a las 7:30 dentista" }' -H "Content-Type=application/json" 172.17.0.2/tree | jq
```

## Useful links

* CONLL-U Format: http://universaldependencies.org/docs/format.html
