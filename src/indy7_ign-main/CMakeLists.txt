cmake_minimum_required(VERSION 3.5)
project(indy7_ign)

# Find dependencies
find_package(ament_cmake REQUIRED)

# Install directories
install(DIRECTORY urdf indy7/meshes DESTINATION share/${PROJECT_NAME})

# Setup the project
ament_package()
