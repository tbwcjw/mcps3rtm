ifeq ($(OS),Windows_NT)
    PYTHON := python
    PLATFORM := windows
    ARCH := $(shell wmic os get osarchitecture | findstr /r /v "^$" | tr -d '\r\n')
else
    PYTHON := python3
    UNAME_S := $(shell uname -s)
    ifeq ($(UNAME_S),Linux)
        PLATFORM := linux
    else ifeq ($(UNAME_S),Darwin)
        PLATFORM := macos
    else
        PLATFORM := unknown
    endif
    ARCH := $(shell uname -m)
endif

VERSION := $(shell $(PYTHON) -c "from cli import __version__; print(__version__)")
APP_NAME = mcps3rtm
SRC = cli.py
DIST_DIR = dist
BUILD_DIR = build
RELEASE_DIR = release
ZIP_FILE = $(RELEASE_DIR)/$(APP_NAME)-$(VERSION)-$(PLATFORM)-$(ARCH).zip

.PHONY: all clean build release

all: clean build release

build:
	pyinstaller --onefile --add-data "wwwroot:wwwroot" --icon=assets/favicon.ico --name $(APP_NAME) $(SRC)

release: build
	@mkdir -p $(RELEASE_DIR)
	@rm -f $(ZIP_FILE)
	@cd $(DIST_DIR) && zip -r ../$(ZIP_FILE) $(APP_NAME)
	@zip -r $(ZIP_FILE) macros config.yml README.md LICENSE

clean:
	@rm -rf $(DIST_DIR) $(BUILD_DIR) __pycache__ $(APP_NAME).spec