parse_settings = {
    'Andriod': {
        'time_regex': r'^(\d{2}-\d{2}\s\d{2}:\d{2}:\d{2}\.\d{3})',
        'time_format': '%m-%d %H:%M:%S.%f',
        'specific': [
            r'((?:true)|(?:false))',
            r'((?<=action=)[^,]+)',
        ],
        'substitute_regex': {
            r'\".*?\"': r'<STR>',
            r'([\w-]+\.){2,}[\w-]+': '<DOMAIN>',
        },
        'split_regex': {
            r'(\w+)=([^\s]*)': r'\1 <\1>',
            r'<bottom of call stack>': '<BOCS>',
            r'[:\s]+': r' ',
        },
    },
    'Apache': {
        'time_regex': r'^\[(.+?)\]',
        'time_format': '%a %b %d %H:%M:%S %Y',
        'specific': [],
        'substitute_regex': {},
        'split_regex': {},
    },
    'BGL': {
        'time_regex': r'\b(\d{4}-\d{2}-\d{2}-\d{2}.\d{2}.\d{2}.\d{6})\b',
        'time_format': '%Y-%m-%d-%H.%M.%S.%f',
        'specific': [],
        'substitute_regex': {
            r'(?<=loading ).*? ': r'<FILE> ',
            r'\/\w+(\/\w+)+\/\w+(\.\w+)?': '<PATH>',
            r'chdir\(.*?\)': 'chdir(<*>()',
            # r'(INFO)|(FATAL)': '<LEVEL>',
        },
        'split_regex': {
            r'(\w+)=([^\s]*)': r'\1 <\1>',
            r'[\.:\s]+': r' ',
        },
    },
    'Hadoop': {
        'time_regex': r'^(\d{4}-\d{2}-\d{2}-\d{2}.\d{2}.\d{2},\d{3})',
        'time_format': '%Y-%m-%d-%H.%M.%S.%f',
        'specific': [],
        'substitute_regex': {
            r'([\w-]+\.){2,}[\w-]+': '<DOMAIN>',
            #r'(\[.*?\])': '<HOST>'
        },
        'split_regex': {},
    },
    'HDFS': {
        'time_regex': r'^(\d{6} \d{6})',
        'time_format': '%y%m%d %H%M%S',
        'specific': [],
        'substitute_regex': {},
        'split_regex': {},
    },
    'HealthApp': {
        'time_regex': r'^(\d{6}-\d{2}:\d{2}:\d{2}:\d{3})',
        'time_format': '%Y%m%d-%H:%M:%S:%f',
        'specific': [],
        'substitute_regex': {},
        'split_regex': {
            r'(\w+)=([^\s]*)': r'\1 <\1>',
            r'[:|\s]+': r' ',
        },
    },
    'HPC': {
        'time_regex': r'\b(\d{10})\b',
        'time_format': '%UNIX_TIMESTAMP',
        'specific': [
            r'((?<=interface )[^\s]+)',
        ],
        'substitute_regex': {},
        'split_regex': {},
    },
    'Linux': {
        'time_regex': r'^(\w{3}\s+\d{1,2} \d{2}:\d{2}:\d{2})',
        'time_format': '%b %d %H:%M:%S',
        'specific': [],
        'substitute_regex': {
            r'(\d+\.){3}\d+(:\d+)? \((([\w-]+\.){2,}[\w-]+)?\)': '<IP> <DOMAIN>',
            r'(?<=user )\b\w+\b': '<USERNAME>',
            # r'\((.*?)\)': r' \1 ',
            # r'\[(.*)\]': r' \1 ',
        },
        'split_regex': {
            r'(\w+)=([^\s]*)': r'\1 <\1>',
        },
    },

    'Mac': {
        'time_regex': r'^(\w{3}\s+\d{1,2} \d{2}:\d{2}:\d{2})',
        'time_format': '%b %d %H:%M:%S',
        'specific': [
            r'((?<=interface )[^\s]+)',
            r'IPV\d',
        ],
        'substitute_regex': {
            # r'(?<=<DATETIME>) [^\s]+\s': ' <HOST> ',
            r'([\w-]+\.){2,}[\w-]+': '<DOMAIN>',
            r'([\w-]+\.){1,}local': '<LOCAL_DOMAIN>',
        },
        'split_regex': {
            r'(\w+)=([^\s]*)': r'\1 <\1>',
            r'[:\(\)",\s]+': r' ',
        },
    },

    'OpenSSH': {
        'time_regex': r'^(\w{3}\s+\d{1,2} \d{2}:\d{2}:\d{2})',
        'time_format': '%b %d %H:%M:%S',
        'specific': [],
        'substitute_regex': {
            r'(?<=user )([^\s]*)': '<USERNAME>',
            r'(?<=for )([^\s]*)': '<USERNAME>',
        },
        'split_regex': {
            r'(\w+)=([^\s]*)': r'\1 <\1>',
        },
        'replace_once': {0},
    },

    'OpenStack': {
        'time_regex': r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}:\d{3})',
        'time_format': '%Y-%m-%d %H:%M:%S:%f',
        'specific': [],
        'substitute_regex': {
            r'\/([\w-]+\/){1,}[\w-]+': '<PATH>',
            # r'([\w-]+\.){2,}[\w-]+': '<DOMAIN>',
            # r'(\[.*?\])': '<HOST>'
        },
        'split_regex': {},
    },

    'Proxifier': {
        'time_regex': r'^\[(\d{2}.\d{2} \d{2}:\d{2}:\d{2})\]',
        'time_format': '%m.%d %H:%M:%S',
        'specific': [],
        'substitute_regex': {
            # r'([\w-]+\.){2,}[\w-]+(:\d+)?': '<DOMAIN>',
            # r'\b[\w-]+.exe( *64)?\b': '<PROGRAM>',
            r'(?<=lifetime )(\d{2}:\d{2})|(<1 sec)': '<LIFETIME>',
            r'\(.*?B\)': '<SIZE>',
        },
        'split_regex': {},
    },

    'Spark': {
        'time_regex': r'^(\d{2}\/\d{2}\/\d{2} \d{2}:\d{2}:\d{2})',
        'time_format': '%y/%m/%d %H:%M:%S',
        'specific': [],
        'substitute_regex': {
            r'\d{1,3}(\.\d{1,3})? [KMGT]?B': '<SIZE>',
        },
        'split_regex': {},
    },

    'Thunderbird': {
        'time_regex': r'\b1(\d{9})\b',
        'time_format': '%UNIX_TIMESTAMP',
        'specific': [],
        'substitute_regex': {
            # r'\/\w+(\/\w+)+\/\w+(\.\w+)?': '<PATH>',
        },
        'split_regex': {
            # r'(\w+)=([^\s]*)': r'\1 <\1>',
        },
    },

    'Windows': {
        'time_regex': r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})',
        'time_format': '%Y-%m-%d %H:%M:%S',
        'specific': [],
        'substitute_regex': {},
        'split_regex': {}

    },

    'Zookeeper': {
        'time_regex': r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3})',
        'time_format': '%Y-%m-%d %H:%M:%S,%f',
        'specific': [],
        'substitute_regex': {
            # r'(\[.*\])': '<HOST>'
        },
        'split_regex': {},
    },
}


parse_settings_plus = {
    'Andriod': {
        'time_regex': r'^(\d{2}-\d{2}\s\d{2}:\d{2}:\d{2}\.\d{3})',
        'time_format': '%m-%d %H:%M:%S.%f',
        'specific': [
            r'((?:true)|(?:false))',
            r'((?<=action=)[^,]+)',
        ],
        'substitute_regex': {
            r'\".*?\"': r'<STR>',
            r'([\w-]+\.){2,}[\w-]+': '<DOMAIN>',
        },
        'split_regex': {
            r'\((.*?)\)': r' \1 ',
            r'(\w+)=([^\s]*)': r'\1 <\1>',
            r'<bottom of call stack>': '<BOCS>',
            r'[:\s]+': r' ',
        },
    },
    'Apache': {
        'time_regex': r'^\[(.+?)\]',
        'time_format': '%a %b %d %H:%M:%S %Y',
        'specific': [],
        'substitute_regex': {},
        'split_regex': {},
    },
    'BGL': {
        'time_regex': r'\b(\d{4}-\d{2}-\d{2}-\d{2}.\d{2}.\d{2}.\d{6})\b',
        'time_format': '%Y-%m-%d-%H.%M.%S.%f',
        'specific': [],
        'substitute_regex': {
            r'(?<=loading ).*? ': r'<FILE> ',
            r'\/\w+(\/\w+)+\/\w+(\.\w+)*': '<PATH>',
            r'chdir\(.*?\)': 'chdir(<*>()',
            # r'(INFO)|(FATAL)': '<LEVEL>',
        },
        'split_regex': {
            r'(\w+)=([^\s]*)': r'\1 <\1>',
            r'[\.:\s]+': r' ',
        },
    },
    'Hadoop': {
        'time_regex': r'^(\d{4}-\d{2}-\d{2}-\d{2}.\d{2}.\d{2},\d{3})',
        'time_format': '%Y-%m-%d-%H.%M.%S.%f',
        'specific': [],
        'substitute_regex': {
            r'([\w-]+\.){2,}[\w-]+': '<DOMAIN>',
            r'\/\w+(\/\w+)*\/[\w\*]+(\.\w+)*': '<PATH>',
            r'(?<= EventType: ).*? ': r'<EVENT_TYPE> ',
            r'(\[.*?\])': '<HOST>',
        },
        'split_regex': {
            r'[:\s]+': r' ',
        },
    },
    'HDFS': {
        'time_regex': r'^(\d{6} \d{6})',
        'time_format': '%y%m%d %H%M%S',
        'specific': [],
        'substitute_regex': {},
        'split_regex': {},
    },
    'HealthApp': {
        'time_regex': r'^(\d{6}-\d{2}:\d{2}:\d{2}:\d{3})',
        'time_format': '%Y%m%d-%H:%M:%S:%f',
        'specific': [],
        'substitute_regex': {},
        'split_regex': {
            r'(\w+)=([^\s]*)': r'\1 <\1>',
            r'[:|\s]+': r' ',
        },
    },
    'HPC': {
        'time_regex': r'\b(\d{10})\b',
        'time_format': '%UNIX_TIMESTAMP',
        'specific': [
            r'((?<=interface )[^\s]+)',
        ],
        'substitute_regex': {},
        'split_regex': {},
    },
    'Linux': {
        'time_regex': r'^(\w{3}\s+\d{1,2} \d{2}:\d{2}:\d{2})',
        'time_format': '%b %d %H:%M:%S',
        'specific': [],
        'substitute_regex': {
            r'(\d+\.){3}\d+(:\d+)? \((([\w-]+\.){2,}[\w-]+)?\)': '<IP> <DOMAIN>',
            r'(?<=user )\b\w+\b': '<USERNAME>',
            r'(\w{3} \w{3}\s+\d{1,2} \d{2}:\d{2}:\d{2} \d{4})': '<DATATIME>',
            # r'\((.*?)\)': r' \1 ',
            # r'\[(.*)\]': r' \1 ',
        },
        'split_regex': {
            r'(\w+)=([^\s]*)': r'\1 <\1>',
        },
    },

    'Mac': {
        'time_regex': r'^(\w{3}\s+\d{1,2} \d{2}:\d{2}:\d{2})',
        'time_format': '%b %d %H:%M:%S',
        'specific': [
            r'((?<=interface )[^\s]+)',
            r'IPV\d',
        ],
        'substitute_regex': {
            # r'(?<=<DATETIME>) [^\s]+\s': ' <HOST> ',
            r'([\w-]+\.){2,}[\w-]+': '<DOMAIN>',
            r'([\w-]+\.){1,}local': '<LOCAL_DOMAIN>',
        },
        'split_regex': {
            r'(\w+)=([^\s]*)': r'\1 <\1>',
            r'[:\(\)",\s]+': r' ',
        },
    },

    'OpenSSH': {
        'time_regex': r'^(\w{3}\s+\d{1,2} \d{2}:\d{2}:\d{2})',
        'time_format': '%b %d %H:%M:%S',
        'specific': [],
        'substitute_regex': {
            r'(?<=user )([^\s]*)': '<USERNAME>',
            r'(?<=for )([^\s]*)': '<USERNAME>',
        },
        'split_regex': {
            r'(\w+)=([^\s]*)': r'\1 <\1>',
        },
        'replace_once': {0},
    },

    'OpenStack': {
        'time_regex': r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}:\d{3})',
        'time_format': '%Y-%m-%d %H:%M:%S:%f',
        'specific': [],
        'substitute_regex': {
            r'\/([\w-]+\/){1,}[\w-]+': '<PATH>',
            # r'([\w-]+\.){2,}[\w-]+': '<DOMAIN>',
            # r'(\[.*?\])': '<HOST>'
        },
        'split_regex': {},
    },

    'Proxifier': {
        'time_regex': r'^\[(\d{2}.\d{2} \d{2}:\d{2}:\d{2})\]',
        'time_format': '%m.%d %H:%M:%S',
        'specific': [],
        'substitute_regex': {
            # r'([\w-]+\.){2,}[\w-]+(:\d+)?': '<DOMAIN>',
            # r'\b[\w-]+.exe( *64)?\b': '<PROGRAM>',
            r'(?<=lifetime )(\d{2}:\d{2})|(<1 sec)': '<LIFETIME>',
            r'\(.*?B\)': '<SIZE>',
        },
        'split_regex': {},
    },

    'Spark': {
        'time_regex': r'^(\d{2}\/\d{2}\/\d{2} \d{2}:\d{2}:\d{2})',
        'time_format': '%y/%m/%d %H:%M:%S',
        'specific': [],
        'substitute_regex': {
            r'\d{1,3}(\.\d{1,3})? [KMGT]?B': '<SIZE>',
        },
        'split_regex': {},
    },

    'Thunderbird': {
        'time_regex': r'\b1(\d{9})\b',
        'time_format': '%UNIX_TIMESTAMP',
        'specific': [],
        'substitute_regex': {
            r'\w{3} \d{1,2} \d{2}:\d{2}:\d{2}': '<DATETIME>',
            r'\/\w+(\/\w+)+\/\w+(\.\w+)?': '<PATH>',
        },
        'split_regex': {
            r'(\w+)=([^\s]*)': r'\1 <\1>',
        },
    },

    'Windows': {
        'time_regex': r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})',
        'time_format': '%Y-%m-%d %H:%M:%S',
        'specific': [],
        'substitute_regex': {},
        'split_regex': {}

    },

    'Zookeeper': {
        'time_regex': r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3})',
        'time_format': '%Y-%m-%d %H:%M:%S,%f',
        'specific': [],
        'substitute_regex': {
            r'(\[.*\])': '<HOST>'
        },
        'split_regex': {},
    },
}