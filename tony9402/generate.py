import json
import os
import ssl
import sys
from typing import Optional, Tuple, Union
from urllib import request
from urllib.error import HTTPError


class color:
    default = "\033[0m"
    black = "\033[0;30m"
    red = "\033[0;31m"
    green = "\033[0;32m"
    yellow = "\033[0;33m"
    blue = "\033[0;34m"
    purple = "\033[0;35m"
    cyan = "\033[0;36m"
    white = "\033[0;37m"


def get_title_of_problem(problem_id: Union[int, str]) -> str:
    ssl_context = ssl._create_unverified_context()
    url = f"https://solved.ac/api/v3/problem/show?problemId={problem_id}"
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        req: request.Request = request.Request(url, headers=headers)
        response = request.urlopen(req, context=ssl_context)
        data = json.loads(response.read().decode("utf-8"))
    except HTTPError as http_error:
        print(
            f"{color.red}[*** API Error] error code: `{http_error.status}` error msg: `{http_error.msg}`"  # type: ignore
        )
        exit(0)

    return data["titleKo"]


def generate_file(problem_id, problem_title, ext="py") -> None:
    path: str = f"[BOJ]_{problem_id}_{problem_title}.{ext}"
    if os.path.exists(path):
        print(f"{color.red}`{path}` is already exists.")
        exit(0)
    open(path, "w").close()
    print(f"{color.green}Generated `{path}` file")


def read_argv(
    first_argv: str, second_argv: Optional[str] = None
) -> Tuple[int, Optional[str]]:
    parsed_ext = None
    try:
        problem_id = int(first_argv)
        parsed_ext = second_argv
    except ValueError:
        try:
            if second_argv is None:
                raise ValueError
            problem_id = int(second_argv)
            parsed_ext = first_argv
        except ValueError:
            print(f"{color.red}Wrong arguments `{first_argv}` `{second_argv}`")
            exit(0)
        except TypeError:
            print(f"{color.red}Wrong arguments `{first_argv}` `{second_argv}`")
            exit(0)
    except Exception:
        print(f"{color.red}Wrong arguments `{first_argv}` `{second_argv}`")
        exit(0)

    ext: str = parsed_ext if parsed_ext else "py"
    return problem_id, ext


if __name__ == "__main__":
    if len(sys.argv) == 3:
        problem_id, ext = read_argv(sys.argv[1], sys.argv[2])
    else:
        problem_id, ext = read_argv(sys.argv[1])
    problem_title = get_title_of_problem(problem_id)
    problem_title = problem_title.replace(" ", "_")
    generate_file(problem_id, problem_title, ext)
