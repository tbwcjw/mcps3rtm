VERSION := $(shell python3 -c "from cli import __version__; print(__version__)")
APP_NAME = mcps3rtm
SRC = cli.py
DIST_DIR = dist
BUILD_DIR = build
RELEASE_DIR = release
ZIP_FILE = $(RELEASE_DIR)/$(APP_NAME)-$(VERSION).zip

.PHONY: all clean build release

all: clean build release

build:
	pyinstaller --onefile --name $(APP_NAME) $(SRC)

release: build
	@mkdir -p $(RELEASE_DIR)
	@rm -f $(ZIP_FILE)
	@cd $(DIST_DIR) && zip -r ../$(ZIP_FILE) $(APP_NAME)
	@zip -r $(ZIP_FILE) macros config.yml README.md

clean:
	@rm -rf $(DIST_DIR) $(BUILD_DIR) __pycache__ *.egg-info $(APP_NAME).spec