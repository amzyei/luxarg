.PHONY: install run

install:
	@echo "Installing..."
	sudo mkdir -p /opt/luxarg/
	sudo cp -rf . /opt/luxarg/ 
	@echo "Creating symlink for main.py..."
	@if [ -f /opt/luxarg/main.py ]; then \
		sudo ln -sf /opt/luxarg/main.py /usr/bin/luxarg; \
	else \
		echo "Warning: main.py not found in $(HOME)/.luxarg, skipping symlink creation."; \
	fi
	@echo "Copying desktop application icon files..."
	@if [ -f ./xdg/luxarg.desktop ]; then \
		sudo cp -rf ./xdg/luxarg.desktop /usr/share/applications; \
		cp -rf ./xdg/luxarg.desktop ~/.local/share/applications; \
	else \
		echo "Warning: luxarg.desktop not found in ./xdg, skipping copy."; \
	fi
	@if [ -f ./icon/luxarg.png ]; then \
		sudo cp -rf ./icon/luxarg.png /usr/share/icons/hicolor/256x256/apps/; \
		sudo cp -rf ./icon/luxarg.png /usr/share/icons/; \
	else \
		echo "Warning: luxarg.png not found in ./icon, skipping copy."; \
	fi
	@echo "Installation complete."

run:
	@echo "Running LuxarG application..."
	python3 main.py
