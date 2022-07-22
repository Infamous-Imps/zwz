# Summer Code Jam 2022 Project by Team Infamous Imps

Team Members:

- [NikzJon](https://github.com/nikhiljohn10) (Team Leader)
- [Arnav](https://github.com/Arnav-2004)
- [Balasai](https://github.com/Sigireddybalasai)
- [Frost](https://github.com/SidmoGoesBrrr)
- [Kalki](https://github.com/Aniket-kr1030)
- [Mercurius13](https://github.com/Mercurius13)


### Dependency

```bash
pip install --user poetry
```

#### Poetry not accessable?

```bash
sudo ln -s /home/$USERNAME/.local/bin/poetry /usr/bin/poetry
```

### Installation

```bash
git clone https://github.com/nikhiljohn10/infamous-imps
cd infamous-imps
poetry install
poetry run task precommit
```

### Linting

```bash
poetry run task lint
```

### Run tests

```bash
poetry run task test
```

### Run development server

```bash
poetry run dev
```
