# Repository Coverage

[Full report](https://htmlpreview.github.io/?https://github.com/gueriboutmathieu/flare_server/blob/python-coverage-comment-action-data/htmlcov/index.html)

| Name                                          |    Stmts |     Miss |   Cover |   Missing |
|---------------------------------------------- | -------: | -------: | ------: | --------: |
| flare/\_\_init\_\_.py                         |        0 |        0 |    100% |           |
| flare/app.py                                  |       39 |       39 |      0% |      1-74 |
| flare/config/\_\_init\_\_.py                  |        0 |        0 |    100% |           |
| flare/config/auth\_config.py                  |        5 |        5 |      0% |       1-7 |
| flare/config/postgresql\_config.py            |        8 |        0 |    100% |           |
| flare/config/youtube\_config.py               |        4 |        0 |    100% |           |
| flare/domain/command\_context.py              |       34 |       17 |     50% |12, 16, 20, 24, 27, 30, 39-52 |
| flare/domain/commands/\_\_init\_\_.py         |        0 |        0 |    100% |           |
| flare/domain/commands/search\_command.py      |        5 |        0 |    100% |           |
| flare/domain/entities/\_\_init\_\_.py         |        0 |        0 |    100% |           |
| flare/domain/entities/channel\_entity.py      |       15 |        0 |    100% |           |
| flare/domain/entities/playlist\_entity.py     |       17 |        0 |    100% |           |
| flare/domain/entities/search\_result.py       |        4 |        0 |    100% |           |
| flare/domain/entities/search\_type.py         |        6 |        0 |    100% |           |
| flare/domain/entities/user\_entity.py         |        8 |        0 |    100% |           |
| flare/domain/entities/video\_entity.py        |       19 |        0 |    100% |           |
| flare/domain/exceptions/\_\_init\_\_.py       |        0 |        0 |    100% |           |
| flare/domain/exceptions/user\_exceptions.py   |        6 |        2 |     67% |      3, 8 |
| flare/repositories/\_\_init\_\_.py            |        0 |        0 |    100% |           |
| flare/repositories/user\_repository.py        |       16 |        5 |     69% | 11, 26-29 |
| flare/routes/\_\_init\_\_.py                  |        0 |        0 |    100% |           |
| flare/routes/auth\_routes.py                  |       24 |       24 |      0% |      1-28 |
| flare/routes/fastapi\_app.py                  |       17 |       17 |      0% |      1-23 |
| flare/routes/search\_routes.py                |       26 |       26 |      0% |      1-34 |
| flare/routes/user\_routes.py                  |        9 |        9 |      0% |      1-12 |
| flare/routes/utils/\_\_init\_\_.py            |        0 |        0 |    100% |           |
| flare/routes/utils/validate\_user\_wrapper.py |        9 |        9 |      0% |      1-12 |
| flare/routes/video\_routes.py                 |       20 |       20 |      0% |      1-29 |
| flare/services/\_\_init\_\_.py                |        0 |        0 |    100% |           |
| flare/services/auth\_service.py               |       18 |        9 |     50% |     14-27 |
| flare/services/search\_service.py             |      137 |       61 |     55% |98-187, 190-199, 202-210, 213-222 |
| flare/services/streaming\_service.py          |       26 |       10 |     62% |27-36, 39-51 |
| flare/utils/parse\_iso\_duration.py           |       12 |        0 |    100% |           |
|                                     **TOTAL** |  **484** |  **253** | **48%** |           |


## Setup coverage badge

Below are examples of the badges you can use in your main branch `README` file.

### Direct image

[![Coverage badge](https://raw.githubusercontent.com/gueriboutmathieu/flare_server/python-coverage-comment-action-data/badge.svg)](https://htmlpreview.github.io/?https://github.com/gueriboutmathieu/flare_server/blob/python-coverage-comment-action-data/htmlcov/index.html)

This is the one to use if your repository is private or if you don't want to customize anything.

### [Shields.io](https://shields.io) Json Endpoint

[![Coverage badge](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/gueriboutmathieu/flare_server/python-coverage-comment-action-data/endpoint.json)](https://htmlpreview.github.io/?https://github.com/gueriboutmathieu/flare_server/blob/python-coverage-comment-action-data/htmlcov/index.html)

Using this one will allow you to [customize](https://shields.io/endpoint) the look of your badge.
It won't work with private repositories. It won't be refreshed more than once per five minutes.

### [Shields.io](https://shields.io) Dynamic Badge

[![Coverage badge](https://img.shields.io/badge/dynamic/json?color=brightgreen&label=coverage&query=%24.message&url=https%3A%2F%2Fraw.githubusercontent.com%2Fgueriboutmathieu%2Fflare_server%2Fpython-coverage-comment-action-data%2Fendpoint.json)](https://htmlpreview.github.io/?https://github.com/gueriboutmathieu/flare_server/blob/python-coverage-comment-action-data/htmlcov/index.html)

This one will always be the same color. It won't work for private repos. I'm not even sure why we included it.

## What is that?

This branch is part of the
[python-coverage-comment-action](https://github.com/marketplace/actions/python-coverage-comment)
GitHub Action. All the files in this branch are automatically generated and may be
overwritten at any moment.