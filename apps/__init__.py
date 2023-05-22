import importlib
import pkgutil

package = __name__
package_path = __path__


def route_views():
    for _, package_name, _ in pkgutil.iter_modules(package_path):
        module_name = f"{package}.{package_name}"
        module = importlib.import_module(module_name)

        if hasattr(module, "route_views"):
            module.route_views()
