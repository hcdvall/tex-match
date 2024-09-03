# Define the Python interpreter and the scripts
PYTHON = python
SCRIPT_1 = src/compare_images.py
SCRIPT_2 = src/aggregate_data.py

# Define the images directory
IMAGE_DIR = resources/DDSTextures

# Define directories for aggregation
AGG_INPUT = observations/
AGG_OUTPUT = results/


# Define example images
EXA1 = skydome_noon_clear_01.dds
EXA2 = Sky_Sunset_01.dds

EXB1 = HV00_radiator_01_s.dds
EXB2 = HV00_radiator_broken_01_s.dds

EXC1 = POI_Black.dds
EXC2 = POI_White.dds

EXD1 = 1951_1C1_tutorial.dds
EXD2 = 1951_1B1_tutorial.dds

# Default target
all: example1

# Run example
example1:
	$(PYTHON) $(SCRIPT_1) $(IMAGE_DIR)/$(EXA1) $(IMAGE_DIR)/$(EXA2)

example2:
	$(PYTHON) $(SCRIPT_1) $(IMAGE_DIR)/$(EXB1) $(IMAGE_DIR)/$(EXB2)

example3:
	$(PYTHON) $(SCRIPT_1) $(IMAGE_DIR)/$(EXC1) $(IMAGE_DIR)/$(EXC2)

example4:
	$(PYTHON) $(SCRIPT_1) $(IMAGE_DIR)/$(EXD1) $(IMAGE_DIR)/$(EXD2)

# Allow for custom image paths
run-custom:
	$(PYTHON) $(SCRIPT_1) $(IMG1) $(IMG2)

# Run aggregation
agg:
	$(PYTHON) $(SCRIPT_2) $(AGG_INPUT) $(AGG_OUTPUT) $(TH)

# Clean target to remove generated output (if applicable)
clean:
	rm -rf observations/

# Help target to show available commands
help:
	@echo "Available commands:"
	@echo "  make example1  - Run example1 with preselected images"
	@echo "  make example2  - Run example2 with preselected images"
	@echo "  make example3  - Run example3 with preselected images"
	@echo "  make example4  - Run example4 with preselected images"	
	@echo "  make run-custom IMG1=<image1> IMG2=<image2> - Compare custom images"
	@echo "  make agg TH=<threshold> - Aggregate data"
	@echo "  make clean    - Clean the output directory"
