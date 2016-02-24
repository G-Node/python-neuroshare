cmake_minimum_required(VERSION 3.0)
project(python_neuroshare)

# mainly used for IDE support (CLion)
# but it can be used to actually build the extension
# for python3 and OSX + homebrew:
# cmake -DPYTHON_EXECUTABLE=/usr/local/bin/python3
#       -DPYTHON_INCLUDE_DIR=`python3-config --prefix`/include/python3.5m
#       -DPYTHON_LIBRARY=`python3-config --prefix`/lib/libpython3.5.dylib ..


find_package(PythonInterp REQUIRED)
find_package(PythonLibs REQUIRED)

message(STATUS "Python version: ${PYTHONLIBS_VERSION_STRING}")

file(WRITE ${CMAKE_CURRENT_BINARY_DIR}/findumpyh.py "try:\n\timport numpy; print(numpy.get_include())\nexcept: pass\n")
exec_program("${PYTHON_EXECUTABLE}"
             ARGS "\"${CMAKE_CURRENT_BINARY_DIR}/findumpyh.py\""
             OUTPUT_VARIABLE NUMPY_PATH)

find_path(PYTHON_NUMPY_HEADER arrayobject.h ${NUMPY_PATH}/numpy)

if(NOT PYTHON_NUMPY_HEADER)
    message(FATAL_ERROR "NumPy header not found")
endif()

message(STATUS "PYTHON_INCLUDE_DIR: ${PYTHON_INCLUDE_DIR}")
message(STATUS "NUMPYP_INCLUDE_DIR: ${NUMPY_PATH}")

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")
include_directories(${PYTHON_INCLUDE_DIR} ${NUMPY_PATH})

set(SOURCE_FILES
    capi/nsAPIdllimp.h
    capi/nsAPItypes.h
    capi/nspy_glue.c)

include_directories(capi)

if(NOT WIN32)
    set(LIBTYPE SHARED)
else()
    set(LIBTYPE MODULE)
endif()

if(NOT ${PYTHONLIBS_VERSION_STRING} VERSION_LESS 3.0)
    exec_program("${PYTHON_EXECUTABLE}-config" ARGS "--extension-suffix"
                 OUTPUT_VARIABLE EXTSUFFIX)
elseif(WIN32 AND NOT CYGWIN)
    set(EXTSUFFIX ".pyd")
else()
    set(EXTSUFFIX ".so")
endif()

MESSAGE(STATUS "Python extension suffix: ${EXTSUFFIX}")

add_library(_capi ${LIBTYPE} ${SOURCE_FILES})
target_link_libraries(_capi ${PYTHON_LIBRARY})
set_target_properties(_capi PROPERTIES PREFIX "")
set_target_properties(_capi PROPERTIES SUFFIX ${EXTSUFFIX})

install(TARGETS _capi DESTINATION ${CMAKE_SOURCE_DIR}/neuroshare)