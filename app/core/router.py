from flask import Flask
from typing import Any, Callable


class Handler:
    def __init__(self, code: int, view_func: Any) -> None:
        self.code = code
        self.view_func = view_func


class Route:
    __rules: list = []
    __endpoints: list = []

    def __init__(self, rule: str, endpoint: str | None = None, view_func: Callable = None,
                 **options) -> None:
        self.rule = rule.strip()
        self.endpoint = endpoint
        self.view_func = view_func

        # TODO : kwargs
        for k, v in options.items():
            setattr(self, k, v)

        assert isinstance(self.rule, str)
        assert self.rule not in self.__class__.__rules, f"rule [{self.rule}] invalid!"
        condition_x = isinstance(self.endpoint, str) and self.endpoint not in self.__class__.__endpoints
        assert not self.endpoint or condition_x, f"endpoint [{self.endpoint}] invalid!"

        self.__class__.__rules.append(self.rule)
        self.__class__.__endpoints.append(self.endpoint)


class Router:
    def __init__(self, app: Flask, routes) -> None:
        self.app = app
        self.routes = routes

        assert isinstance(
            app, Flask), "The app instance should be Flask application instance"
        assert isinstance(routes, list) and len(
            routes) > 0, "routes must be a list and none empty"

        self.generate()

    def generate(self) -> None:
        for route in self.routes:

            if isinstance(route, Handler):
                self.app.register_error_handler(route.code, route.view_func)
            else:
                # print(vars(route))
                self.app.add_url_rule(**vars(route))
