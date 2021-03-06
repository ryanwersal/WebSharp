##
# Portions Copyright (c) Microsoft Corporation. All rights reserved. 
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#  http://www.apache.org/licenses/LICENSE-2.0  
#
# THIS CODE IS PROVIDED *AS IS* BASIS, WITHOUT WARRANTIES OR CONDITIONS
# OF ANY KIND, EITHER EXPRESS OR IMPLIED, INCLUDING WITHOUT LIMITATION 
# ANY IMPLIED WARRANTIES OR CONDITIONS OF TITLE, FITNESS FOR A PARTICULAR 
# PURPOSE, MERCHANTABLITY OR NON-INFRINGEMENT. 
#
# See the Apache Version 2.0 License for specific language governing 
# permissions and limitations under the License.
##
{
  'targets': [
    {
      'target_name': 'edge_coreclr',
      'win_delay_load_hook': 'false',
      'include_dirs': [
        "<!(node -e \"require('nan')\")"
      ],
      'cflags+': [
        '-DHAVE_CORECLR -D_NO_ASYNCRTIMP -std=c++11 -Wno-reorder -Wno-sign-compare -Wno-mismatched-tags -Wno-missing-braces -Wno-redundant-move -Wno-deprecated-declarations -Wno-unused-private-field -Wno-unused-variable'
      ],
      'cflags!': [
        '-fno-exceptions',
        '-Wsign-compare',
        '-Wreorder',
        '-Wmismatched-tags',
        '-Wmissing-braces',
        '-Wredundant-move',
        '-Wdeprecated-declarations',
        '-Wunused-private-field',
        '-Wunused-variable'
      ],
      'cflags_cc!': [
        '-fno-exceptions',
        '-Wsign-compare',
        '-Wreorder',
        '-Wmismatched-tags',
        '-Wmissing-braces',
        '-Wredundant-move',
        '-Wdeprecated-declarations',
        '-Wunused-private-field',
        '-Wunused-variable'
      ],
      'xcode_settings': {
        'OTHER_CFLAGS': [
          '-DHAVE_CORECLR -D_NO_ASYNCRTIMP -Wno-reorder -Wno-sign-compare -Wno-mismatched-tags -Wno-missing-braces -Wno-redundant-move -Wno-deprecated-declarations -Wno-unused-private-field -Wno-unused-variable'
        ],
        'GCC_ENABLE_CPP_EXCEPTIONS': 'YES',
        'GCC_ENABLE_CPP_RTTI': 'YES',
        'CLANG_CXX_LANGUAGE_STANDARD': 'c++11',
        'CLANG_CXX_LIBRARY': 'libc++',
        'MACOSX_DEPLOYMENT_TARGET': '10.7'
      },
      'sources+': [
        'src/common/v8synchronizationcontext.cpp',
        'src/common/edge.cpp',
        'src/CoreCLREmbedding/coreclrembedding.cpp',
        'src/CoreCLREmbedding/coreclrfunc.cpp',
        'src/CoreCLREmbedding/coreclrnodejsfunc.cpp',
        'src/CoreCLREmbedding/coreclrfuncinvokecontext.cpp',
        'src/CoreCLREmbedding/coreclrnodejsfuncinvokecontext.cpp',
        'src/common/utils.cpp',
        'src/CoreCLREmbedding/pal/pal_utils.cpp',
        'src/CoreCLREmbedding/pal/trace.cpp',
        'src/CoreCLREmbedding/fxr/fx_ver.cpp',
        'src/CoreCLREmbedding/fxr/fx_muxer.cpp',
        'src/CoreCLREmbedding/json/casablanca/src/json/json.cpp',
        'src/CoreCLREmbedding/json/casablanca/src/json/json_parsing.cpp',
        'src/CoreCLREmbedding/json/casablanca/src/json/json_serialization.cpp',
        'src/CoreCLREmbedding/json/casablanca/src/utilities/asyncrt_utils.cpp',
        'src/CoreCLREmbedding/deps/deps_format.cpp',
        'src/CoreCLREmbedding/deps/deps_entry.cpp',
        'src/CoreCLREmbedding/deps/deps_resolver.cpp',
        'src/CoreCLREmbedding/host/args.cpp',
        'src/CoreCLREmbedding/host/coreclr.cpp',
        'src/CoreCLREmbedding/host/libhost.cpp',
        'src/CoreCLREmbedding/host/runtime_config.cpp'
      ],
      'include_dirs+': [
        'src/CoreCLREmbedding/json/casablanca/include'
      ],
      'conditions': [
        [
          'OS=="win"',
          {
            'sources+': [
              'src/CoreCLREmbedding/pal/pal.windows.cpp',
            ]
          },
          {
            'sources+': [
              'src/CoreCLREmbedding/pal/pal.unix.cpp'
            ]
          }
        ]
      ],
      'configurations': {
        'Release': {
          'msvs_settings': {
            'VCCLCompilerTool': {
              # this is out of range and will generate a warning and skip adding RuntimeLibrary property:
              'RuntimeLibrary': -1,
              # this is out of range and will generate a warning and skip adding RuntimeTypeInfo property:
              'RuntimeTypeInfo': -1,
              'BasicRuntimeChecks': -1,
              'ExceptionHandling': '0',
              'AdditionalOptions': [
                '/wd4506',
                '/DHAVE_CORECLR',
                '/EHsc',
                '/D_NO_ASYNCRTIMP',
                '/D_HAS_EXCEPTIONS'
              ]
            },
            'VCLinkerTool': {
              'AdditionalOptions': [
                '/ignore:4248',
                'shlwapi.lib'
              ]
            }
          }
        },
        'Debug': {
          'msvs_settings': {
            'VCCLCompilerTool': {
              # this is out of range and will generate a warning and skip adding RuntimeLibrary property:
              'RuntimeLibrary': 3,
              # this is out of range and will generate a warning and skip adding RuntimeTypeInfo property:
              'RuntimeTypeInfo': -1,
              'BasicRuntimeChecks': -1,
              'ExceptionHandling': '0',
              'AdditionalOptions': [
                '/wd4506',
                '/DHAVE_CORECLR',
                '/D_NO_ASYNCRTIMP',
                '/D_HAS_EXCEPTIONS'
                '/EHsc',
				'/MDd'
              ]
            },
            'VCLinkerTool': {
              'AdditionalOptions': [
                '/ignore:4248',
                'shlwapi.lib'
              ]
            }
          }
        }
      }
    },
    {
      'variables': {
        'MONO_PKG_CONFIG': '/Library/Frameworks/Mono.framework/Versions/Current/bin/pkg-config'
      },
      'target_name': 'edge_nativeclr',
      'win_delay_load_hook': 'false',
      'include_dirs': [
        "<!(node -e \"require('nan')\")"
      ],
      'cflags+': [
        '-DHAVE_NATIVECLR -std=c++11'
      ],
      'xcode_settings': {
        'OTHER_CFLAGS': [
          '-DHAVE_NATIVECLR'
        ]
      },
      'conditions': [
        [
          'OS=="win"',
          {
            'sources+': [
              'src/dotnet/utils.cpp',
              'src/dotnet/clrfunc.cpp',
              'src/dotnet/clrfuncinvokecontext.cpp',
              'src/dotnet/nodejsfunc.cpp',
              'src/dotnet/nodejsfuncinvokecontext.cpp',
              'src/dotnet/persistentdisposecontext.cpp',
              'src/dotnet/clrfuncreflectionwrap.cpp',
              'src/dotnet/clractioncontext.cpp',
              'src/common/v8synchronizationcontext.cpp',
              'src/common/edge.cpp'
            ]
          },
          {
            'conditions': [
              [
                '"<!((which mono 2>/dev/null) || echo not_found)"!="not_found"',
                {
                  'sources+': [
                    'src/mono/clractioncontext.cpp',
                    'src/mono/clrfunc.cpp',
                    'src/mono/clrfuncinvokecontext.cpp',
                    'src/mono/monoembedding.cpp',
                    'src/mono/task.cpp',
                    'src/mono/dictionary.cpp',
                    'src/mono/nodejsfunc.cpp',
                    'src/mono/nodejsfuncinvokecontext.cpp',
                    'src/mono/utils.cpp',
                    'src/common/utils.cpp',
                    'src/common/v8synchronizationcontext.cpp',
                    'src/common/edge.cpp'
                  ],
                  'conditions': 
                  [
                    [
                      '"<!((pkg-config mono-2 --libs 2>/dev/null) || echo not_found)"!="not_found"',
                      {
                            'include_dirs': [
                              '<!@(pkg-config mono-2 --cflags-only-I | sed s/-I//g)'
                            ],
                            'link_settings': {
                              'libraries': [
                                '<!@(pkg-config mono-2 --libs)'
                              ]
                            }
                      },
                      '"<!((pkg-config mono-2 --libs 2>/dev/null) || echo not_found)"=="not_found"',
                      {
                            'include_dirs': [
                              '<!@(<(MONO_PKG_CONFIG) mono-2 --cflags-only-I | sed s/-I//g)'
                            ],
                            'link_settings': {
                              'libraries': [
                                '<!@(<(MONO_PKG_CONFIG) mono-2 --libs)'
                              ]
                            }
                      }
                    ]
                  ],
                },
                {
                  'type': 'none'
                }
              ]
            ]
          }
        ]
      ],
      'configurations': {
        'Release': {
          'msvs_settings': {
            'VCCLCompilerTool': {
              # this is out of range and will generate a warning and skip adding RuntimeLibrary property:
              'RuntimeLibrary': -1,
              # this is out of range and will generate a warning and skip adding RuntimeTypeInfo property:
              'RuntimeTypeInfo': -1,
              'BasicRuntimeChecks': -1,
              'ExceptionHandling': '0',
              'AdditionalOptions': [
                '/clr',
                '/wd4506',
                '/DHAVE_NATIVECLR'
              ]
            },
            'VCLinkerTool': {
              'AdditionalOptions': [
                '/ignore:4248'
              ]
            }
          }
        },
        'Debug': {
          'msvs_settings': {
            'VCCLCompilerTool': {
              # this is out of range and will generate a warning and skip adding RuntimeLibrary property:
              'RuntimeLibrary': 3,
              # this is out of range and will generate a warning and skip adding RuntimeTypeInfo property:
              'RuntimeTypeInfo': -1,
              'BasicRuntimeChecks': -1,
              'ExceptionHandling': '0',
              'AdditionalOptions': [
                '/clr',
                '/wd4506',
                '/DHAVE_NATIVECLR',
				'/MDd'
              ]
            },
            'VCLinkerTool': {
              'AdditionalOptions': [
                '/ignore:4248'
              ]
            }
          }
        }
      }
    },
    {
      'variables': {
        'conditions': [
          ['target_arch=="ia32"', {
            'DEFAULT_MONO_ROOT': 'C:\Program Files %28x86%29\Mono'
          }],
          ['target_arch=="x64"', {
            'DEFAULT_MONO_ROOT': 'C:\Program Files\Mono'
          }],
        ],
      },
      'target_name': 'edge_monoclr',
      'win_delay_load_hook': 'false',
      'include_dirs': [
        "<!(node -e \"require('nan')\")",
		    '<(DEFAULT_MONO_ROOT)\include\mono-2.0'
      ],
      'cflags+': [
        '-DHAVE_NATIVECLR -std=c++11'
      ],
      'xcode_settings': {
        'OTHER_CFLAGS': [
          '-DHAVE_NATIVECLR'
        ]
      },
      'conditions': [
        [
          'OS=="win"',
          {
			'conditions': [
              [
                '"<!(node -e \"require(\'./tools/gyp-whereis.js\')(\'mono.exe\')\")"!="null"',
                {
					'sources+': [
						   'src/mono/clractioncontext.cpp',
							'src/mono/clrfunc.cpp',
							'src/mono/clrfuncinvokecontext.cpp',
						   'src/mono/monoembedding.cpp',
						   'src/mono/task.cpp',
						   'src/mono/dictionary.cpp',
						   'src/mono/nodejsfunc.cpp',
						   'src/mono/nodejsfuncinvokecontext.cpp',
						   'src/mono/utils.cpp',
							'src/common/v8synchronizationcontext.cpp',
							'src/common/edge.cpp'
					]
				},
        {
                  'type': 'none'
                }
			  ]
			]
          }
        ]
      ],
      'configurations': {
        'Release': {
          'msvs_settings': {
            'VCCLCompilerTool': {
              # this is out of range and will generate a warning and skip adding RuntimeLibrary property:
              'RuntimeLibrary': -1,
              # this is out of range and will generate a warning and skip adding RuntimeTypeInfo property:
              'RuntimeTypeInfo': -1,
              'BasicRuntimeChecks': -1,
              'ExceptionHandling': '0',
              'AdditionalOptions': [
                '/clr',
                '/wd4506',
				'/DHAVE_NATIVECLR',
                '/DHAVE_MONO'
              ]
            },
            'VCLinkerTool': {
			  'AdditionalDependencies' :
			  [
				'mono-2.0.lib'
			  ],
			  'AdditionalLibraryDirectories' :
			  [
				'<(DEFAULT_MONO_ROOT)\lib'
			  ],
              'AdditionalOptions': [
                '/ignore:4248'
              ]
            }
          }
        },
        'Debug': {
          'msvs_settings': {
            'VCCLCompilerTool': {
              # this should be /MDd but not being set properly so it is overridden in AdditionalOptions:
              'RuntimeLibrary': 3,
              # this is out of range and will generate a warning and skip adding RuntimeTypeInfo property:
              'RuntimeTypeInfo': -1,
              'BasicRuntimeChecks': -1,
              'ExceptionHandling': '0',
              'AdditionalOptions': [
                '/clr',
                '/wd4506',
                '/DHAVE_NATIVECLR',
                '/DHAVE_MONO',
				'/MDd'
              ]
            },
            'VCLinkerTool': {
			  'AdditionalDependencies' :
			  [
				'mono-2.0.lib'
			  ],
			  'AdditionalLibraryDirectories' :
			  [
				'<(DEFAULT_MONO_ROOT)\lib'
			  ],
			  'AdditionalOptions': [
                '/ignore:4248'
              ]
            }
          }
        }
      }
    },
    {
      'target_name': 'build_managed',
      'type': 'none',
      'dependencies': [
        'edge_nativeclr',
        'edge_coreclr'
      ],
      'conditions': [
        [
          'OS=="win"',
          {
			        'conditions': [
                [
                  '"<!(node -e \"require(\'./tools/gyp-whereis.js\')(\'mono.exe\')\")"!="null"',
                  {
                 'actions+': [
                    {
                      'action_name': 'compile_mono_embed',
                      'inputs': [
                        'src/mono/*.cs'
                      ],
                      'outputs': [
                        '$(ConfigurationName)/monoembedding.exe'
                      ],
                      'action': [
                        'csc',
                        '-target:exe',
                        '-out:$(ConfigurationName)/MonoEmbedding.exe',
                        'src/mono/*.cs',
                        'src/common/*.cs'
                      ]
                    }
                  ]                    
				          }
			          ]
			        ]            
          },
          {
            'conditions': [
              [
                '"<!((which mono 2>/dev/null) || echo not_found)"!="not_found"',
                {
                  'actions+': [
                    {
                      'action_name': 'compile_mono_embed',
                      'inputs': [
                        'src/mono/*.cs'
                      ],
                      'outputs': [
                        'build/$(BUILDTYPE)/monoembedding.exe'
                      ],
                      'action': [
                        'dmcs',
                        '-sdk:4.5',
                        '-target:exe',
                        '-out:build/$(BUILDTYPE)/MonoEmbedding.exe',
                        'src/mono/*.cs',
                        'src/common/*.cs'
                      ]
                    }
                  ]
                }
              ],
              [
                '"<!((which dotnet 2>/dev/null) || echo not_found)"!="not_found"',
                {
                  'actions+': [
                    {
                      'action_name': 'restore_bootstrap_packages',
                      'inputs': [
                        'lib/bootstrap/project.json'
                      ],
                      'outputs': [
                        'lib/bootstrap/project.lock.json'
                      ],
                      'action': [
                        'bash',
                        '-c',
                        'cd lib/bootstrap && dotnet restore'
                      ]
                    },
                    {
                      'action_name': 'compile_bootstrap',
                      'inputs': [
                        'lib/bootstrap/*.cs'
                      ],
                      'outputs': [
                        'lib/bootstrap/bin/$(BUILDTYPE)/netstandard1.6/bootstrap.dll'
                      ],                        
                      'action': [
                        'bash',
                        '-c',
                        'cd lib/bootstrap && dotnet build --configuration $(BUILDTYPE)'
                      ]
                    }
                  ]
                }
              ]
            ]
          }
        ]
      ]
    }
  ]
}