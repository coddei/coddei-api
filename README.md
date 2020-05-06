<br />
<p align="center">
    <a href="https://www.coddei.com">
        <img src="https://i.imgur.com/03bCh2l.png" width=80%>
    </a>
</p>
<br />

# Coddei API
API feita em [Pyramid](https://trypyramid.com/) para ser utilizada em conjunto com o [CoddeiBot](https://github.com/coddei/coddei-bot) no servidor da [Coddei](https://www.coddei.com) no Discord.

## Instalação

Precisa do [MongoDB](https://www.mongodb.com/) instalado

```bash
python -m venv env

# Windows
env/Scripts/pip install -e .

# Linux
env/bin/pip install -e .
```

## Para rodar
```bash
# Windows
env/Scripts/pserve development.ini --reload

# Linux
env/bin/pserve development.ini --reload
```
