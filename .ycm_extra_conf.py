# This file is NOT licensed under the GPLv4, which is the license for the rest
# of YouCompleteMe.
#
# Here's the license text for this file:
#
# This is free and unencumbered software released into the public domain.
#
# Anyone is free to copy, modify, publish, use, compile, sell, or
# distribute this software, either in source code form or as a compiled
# binary, for any purpose, commercial or non-commercial, and by any
# means.
#
# In jurisdictions that recognize copyright laws, the author or authors
# of this software dedicate any and all copyright interest in the
# software to the public domain. We make this dedication for the benefit
# of the public at large and to the detriment of our heirs and
# successors. We intend this dedication to be an overt act of
# relinquishment in perpetuity of all present and future rights to this
# software under copyright law.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
# OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
# ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.
#
# For more information, please refer to <http://unlicense.org/>

import os
import ycm_core

# These are the compilation flags that will be used in case there's no
# compilation database set (by default, one is not set).
# CHANGE THIS LIST OF FLAGS. YES, THIS IS THE DROID YOU HAVE BEEN LOOKING FOR.
flags = [
        # THIS IS IMPORTANT! Without a "-std=<something>" flag, clang won't know which
        # language to use when compiling headers. So it will guess. Badly. So C++
        # headers will be compiled as C headers. You don't want that so ALWAYS specify
        # a "-std=<something>".
        # For a C project, you would set this to something like 'c99' instead of
        # 'c++11'.
        '-std=c99',
        # ...and the same thing goes for the magic -x option which specifies the
        # language that the files to be compiled are written in. This is mostly
        # relevant for c++ headers.
        # For a C project, you would set this to 'c' instead of 'c++'.
        '-x',
        'c',

        #System Header Files Path, Like #include <Header.h>
        
        # For Linux system
        '-isystem','/usr/include',
        '-isystem','/usr/include/c++/4.8',
        '-isystem','/usr/include/c++/5.2.1/',
        
        # For windows system And IAR
        '-system','C:\Program Files (x86)\IAR Systems\Embedded Workbench 7.3\arm\inc\c',


        # User Compile FLAGS

        # For Qt Project
        #'-DQT_CORE_LIB',
        #'-DQT_GUI_LIB',
        #'-DQT_NETWORK_LIB',
        #'-DQT_QML_LIB',
        #'-DQT_QUICK_LIB',
        #'-DQT_SQL_LIB',
        #'-DQT_WIDGETS_LIB',
        #'-DQT_XML_LIB',
        #'-D__PIC__'

        # For STM32 Project
        '-DUSE_STDPERIPH_DRIVER',
        #'-DSTM32F10X_HD',
        '-DHSE_VALUE_16M',
        '-DSTM32F37X',

        #User Header Files Path, Like #include "Header.h"
        # STM32 F0
        #'-I','/media/zh/Work/STM32Library/F0/CMSIS/Include',
        #'-I','/media/zh/Work/STM32Library/F0/CMSIS/ST/STM32F0xx/Include',
        #'-I','/media/zh/Work/STM32Library/F0/STM32F0xx_StdPeriph_Driver/inc',

        # STM32 F1
        #'-I','/media/zh/Work/STM32Library/F1/STM32F10x_StdPeriph_Driver/inc/',
        #'-I','/media/zh/Work/STM32Library/F1/CMSIS/CM3/CoreSupport/',
        #'-I','/media/zh/Work/STM32Library/F1/CMSIS/CM3/DeviceSupport/ST/STM32F10x/',
        #'-I','/media/zh/Work/STM32Library/F1/CMSIS/CM3/DeviceSupport/ST/STM32F10x/startup/iar/',
        
        # STM32 F3

        '-I','D:/STM32Library/F3/CMSIS/Include',
        '-I','D:/STM32Library/F3/CMSIS/Device/ST/STM32F37x/Include',
        '-I','D:/STM32Library/F3/STM32F37x_StdPeriph_Driver/inc',
        '-I','/media/zh/Work/STM32Library/F3/CMSIS/Include',
        '-I','/media/zh/Work/STM32Library/F3/CMSIS/Device/ST/STM32F37x/Include',
        '-I','/media/zh/Work/STM32Library/F3/STM32F37x_StdPeriph_Driver/inc',

        # Current Project
        
        '-I','D:/Project/DustMeasure/code/SecondMeter',
        '-I','/media/zh/Work/Project/DustMeasure/code/SecondMeter',



        # Qt header dir

        #'-I','/home/zh/Qt5.5.1/5.5/gcc_64/include/',
        #'-I','/home/zh/Qt5.5.1/5.5/gcc_64/include/Enginio/',
        #'-I','/home/zh/Qt5.5.1/5.5/gcc_64/include/list',
        #'-I','/home/zh/Qt5.5.1/5.5/gcc_64/include/QtBluetooth/',
        #'-I','/home/zh/Qt5.5.1/5.5/gcc_64/include/QtCLucene/',
        #'-I','/home/zh/Qt5.5.1/5.5/gcc_64/include/QtConcurrent/',
        #'-I','/home/zh/Qt5.5.1/5.5/gcc_64/include/QtCore/',
        #'-I','/home/zh/Qt5.5.1/5.5/gcc_64/include/QtDBus/',
        #'-I','/home/zh/Qt5.5.1/5.5/gcc_64/include/QtDeclarative/',
        #'-I','/home/zh/Qt5.5.1/5.5/gcc_64/include/QtDesigner/',
        #'-I','/home/zh/Qt5.5.1/5.5/gcc_64/include/QtDesignerComponents/',
        #'-I','/home/zh/Qt5.5.1/5.5/gcc_64/include/QtGui/',
        #'-I','/home/zh/Qt5.5.1/5.5/gcc_64/include/QtHelp/',
        #'-I','/home/zh/Qt5.5.1/5.5/gcc_64/include/QtLocation/',
        #'-I','/home/zh/Qt5.5.1/5.5/gcc_64/include/QtMultimedia/',
        #'-I','/home/zh/Qt5.5.1/5.5/gcc_64/include/QtMultimediaQuick_p/',
        #'-I','/home/zh/Qt5.5.1/5.5/gcc_64/include/QtMultimediaWidgets/',
        #'-I','/home/zh/Qt5.5.1/5.5/gcc_64/include/QtNetwork/',
        #'-I','/home/zh/Qt5.5.1/5.5/gcc_64/include/QtNfc/',
        #'-I','/home/zh/Qt5.5.1/5.5/gcc_64/include/QtOpenGL/',
        #'-I','/home/zh/Qt5.5.1/5.5/gcc_64/include/QtOpenGLExtensions/',
        #'-I','/home/zh/Qt5.5.1/5.5/gcc_64/include/QtPlatformHeaders/',
        #'-I','/home/zh/Qt5.5.1/5.5/gcc_64/include/QtPlatformSupport/',
        #'-I','/home/zh/Qt5.5.1/5.5/gcc_64/include/QtPositioning/',
        #'-I','/home/zh/Qt5.5.1/5.5/gcc_64/include/QtPrintSupport/',
        #'-I','/home/zh/Qt5.5.1/5.5/gcc_64/include/QtQml/',
        #'-I','/home/zh/Qt5.5.1/5.5/gcc_64/include/QtQuick/',
        #'-I','/home/zh/Qt5.5.1/5.5/gcc_64/include/QtQuickParticles/',
        #'-I','/home/zh/Qt5.5.1/5.5/gcc_64/include/QtQuickTest/',
        #'-I','/home/zh/Qt5.5.1/5.5/gcc_64/include/QtQuickWidgets/',
        #'-I','/home/zh/Qt5.5.1/5.5/gcc_64/include/QtScript/',
        #'-I','/home/zh/Qt5.5.1/5.5/gcc_64/include/QtScriptTools/',
        #'-I','/home/zh/Qt5.5.1/5.5/gcc_64/include/QtSensors/',
        #'-I','/home/zh/Qt5.5.1/5.5/gcc_64/include/QtSerialPort/',
        #'-I','/home/zh/Qt5.5.1/5.5/gcc_64/include/QtSql/',
        #'-I','/home/zh/Qt5.5.1/5.5/gcc_64/include/QtSvg/',
        #'-I','/home/zh/Qt5.5.1/5.5/gcc_64/include/QtTest/',
        #'-I','/home/zh/Qt5.5.1/5.5/gcc_64/include/QtUiTools/',
        #'-I','/home/zh/Qt5.5.1/5.5/gcc_64/include/QtWebChannel/',
        #'-I','/home/zh/Qt5.5.1/5.5/gcc_64/include/QtWebEngine/',
        #'-I','/home/zh/Qt5.5.1/5.5/gcc_64/include/QtWebEngineWidgets/',
        #'-I','/home/zh/Qt5.5.1/5.5/gcc_64/include/QtWebKit/',
        #'-I','/home/zh/Qt5.5.1/5.5/gcc_64/include/QtWebKitWidgets/',
        #'-I','/home/zh/Qt5.5.1/5.5/gcc_64/include/QtWebSockets/',
        #'-I','/home/zh/Qt5.5.1/5.5/gcc_64/include/QtWebView/',
        #'-I','/home/zh/Qt5.5.1/5.5/gcc_64/include/QtWidgets/',
        #'-I','/home/zh/Qt5.5.1/5.5/gcc_64/include/QtX11Extras/',
        #'-I','/home/zh/Qt5.5.1/5.5/gcc_64/include/QtXml/',
        #'-I','/home/zh/Qt5.5.1/5.5/gcc_64/include/QtXmlPatterns/',
        #'-I','/home/zh/Qt5.5.1/5.5/gcc_64/include/QtZlib/',
        ]

# Set this to the absolute path to the folder (NOT the file!) containing the
# compile_commands.json file to use that instead of 'flags'. See here for
# more details: http://clang.llvm.org/docs/JSONCompilationDatabase.html
#
# You can get CMake to generate this file for you by adding:
#   set( CMAKE_EXPORT_COMPILE_COMMANDS 1 )
# to your CMakeLists.txt file.
#
# Most projects will NOT need to set this to anything; you can just change the
# 'flags' list of compilation flags. Notice that YCM itself uses that approach.
compilation_database_folder = ''

if os.path.exists( compilation_database_folder ):
  database = ycm_core.CompilationDatabase( compilation_database_folder )
else:
  database = None

SOURCE_EXTENSIONS = [ '.cpp', '.cxx', '.cc', '.c', '.m', '.mm' ]

def DirectoryOfThisScript():
  return os.path.dirname( os.path.abspath( __file__ ) )


def MakeRelativePathsInFlagsAbsolute( flags, working_directory ):
  if not working_directory:
    return list( flags )
  new_flags = []
  make_next_absolute = False
  path_flags = [ '-isystem', '-I', '-iquote', '--sysroot=' ]
  for flag in flags:
    new_flag = flag

    if make_next_absolute:
      make_next_absolute = False
      if not flag.startswith( '/' ):
        new_flag = os.path.join( working_directory, flag )

    for path_flag in path_flags:
      if flag == path_flag:
        make_next_absolute = True
        break

      if flag.startswith( path_flag ):
        path = flag[ len( path_flag ): ]
        new_flag = path_flag + os.path.join( working_directory, path )
        break

    if new_flag:
      new_flags.append( new_flag )
  return new_flags


def IsHeaderFile( filename ):
  extension = os.path.splitext( filename )[ 1 ]
  return extension in [ '.h', '.hxx', '.hpp', '.hh' ]


def GetCompilationInfoForFile( filename ):
  # The compilation_commands.json file generated by CMake does not have entries
  # for header files. So we do our best by asking the db for flags for a
  # corresponding source file, if any. If one exists, the flags for that file
  # should be good enough.
  if IsHeaderFile( filename ):
    basename = os.path.splitext( filename )[ 0 ]
    for extension in SOURCE_EXTENSIONS:
      replacement_file = basename + extension
      if os.path.exists( replacement_file ):
        compilation_info = database.GetCompilationInfoForFile(
          replacement_file )
        if compilation_info.compiler_flags_:
          return compilation_info
    return None
  return database.GetCompilationInfoForFile( filename )


def FlagsForFile( filename, **kwargs ):
  if database:
    # Bear in mind that compilation_info.compiler_flags_ does NOT return a
    # python list, but a "list-like" StringVec object
    compilation_info = GetCompilationInfoForFile( filename )
    if not compilation_info:
      return None

    final_flags = MakeRelativePathsInFlagsAbsolute(
      compilation_info.compiler_flags_,
      compilation_info.compiler_working_dir_ )

    # NOTE: This is just for YouCompleteMe; it's highly likely that your project
    # does NOT need to remove the stdlib flag. DO NOT USE THIS IN YOUR
    # ycm_extra_conf IF YOU'RE NOT 100% SURE YOU NEED IT.
    try:
      final_flags.remove( '-stdlib=libc++' )
    except ValueError:
      pass
  else:
    relative_to = DirectoryOfThisScript()
    final_flags = MakeRelativePathsInFlagsAbsolute( flags, relative_to )

  return {
    'flags': final_flags,
    'do_cache': True
  }
