import os
import pkgutil
import importlib
import logging
import logging.config
from dotenv import load_dotenv
from calculator.commands import CommandHandler, Command

class Calculator:
    def __init__(self):
        os.makedirs('logs', exist_ok=True)  # Ensure logs directory exists
        self.configure_logging()  # Configure logging before other operations
        logging.info("Logger successfully configured.")
        
        load_dotenv()  # Load environment variables from .env
        logging.info("Environment variables loaded.")

        self.command_handler = CommandHandler()  # Initialize command handler
        logging.info("Command handler initialized.")


    def configure_logging(self):
        """Configure logging with file and console handlers."""
        logging_conf_path = 'logging.conf'
        if os.path.exists(logging_conf_path):
            logging.config.fileConfig(logging_conf_path, disable_existing_loggers=False)
        else:
            logging.basicConfig(
                level=logging.INFO,
                format="%(asctime)s - %(levelname)s - %(message)s",
                handlers=[
                    logging.FileHandler("logs/calculator.log"),  # Logs to file
                    logging.StreamHandler()  # Logs to console
                ]
            )
        logging.info("Logging configured.")

    def load_plugins(self):
        """Dynamically load all plugins in the 'calculator.plugins' directory."""
        plugins_package = 'calculator.plugins'
        try:
            package_path = importlib.import_module(plugins_package).__path__
        except ModuleNotFoundError:
            logging.warning(f"Plugins package '{plugins_package}' not found.")
            return

        for _, plugin_name, is_pkg in pkgutil.iter_modules(package_path):
            if is_pkg:
                try:
                    plugin_module = importlib.import_module(f'{plugins_package}.{plugin_name}')
                    self.register_plugin_commands(plugin_module, plugin_name)
                except ImportError as e:
                    logging.error(f"Error importing plugin {plugin_name}: {e}")

    def register_plugin_commands(self, plugin_module, plugin_name):
        """Registers plugin commands dynamically."""
        for item_name in dir(plugin_module):
            item = getattr(plugin_module, item_name)
            if isinstance(item, type) and issubclass(item, Command) and item is not Command:
                command_name = getattr(item, "name", plugin_name)  # Allow explicit command names
                try:
                    if command_name.lower() == "menu":  
                        # Only pass handler if required (for MenuCommand)
                        self.command_handler.register_command(command_name, item(self.command_handler))
                    else:
                        # Instantiate normally for all other commands
                        self.command_handler.register_command(command_name, item())

                    logging.info(f"Command '{command_name}' from plugin '{plugin_name}' registered.")
                except TypeError as e:
                    logging.error(f"Error instantiating command '{command_name}': {e}")


    def start(self):
        """Starts the calculator application with a REPL loop."""
        self.load_plugins()
        logging.info("Calculator started. Type 'exit' to exit.")
        try:
            while True:
                cmd_input = input(">>> ").strip()
                if cmd_input.lower() == 'exit':
                    logging.info("Calculator exited.")
                    break
                try:
                    self.command_handler.execute_command(cmd_input)
                except KeyError:
                    logging.error(f"Unknown command: {cmd_input}. Try again.")
        except KeyboardInterrupt:
            logging.info("Calculator interrupted and exiting gracefully.")
        finally:
            logging.info("Calculator shutdown.")

if __name__ == "__main__":
    calculator = Calculator()
    calculator.start()
