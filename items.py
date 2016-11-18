pkg_dnf = {
    'htop': {},
}

files = {
    '/root/.config/htop/htoprc': {
        'source': "htoprc",
        'owner': "root",
        'mode': "0640",
        'content_type': "text",
        'needs': [
            "pkg_dnf:htop",
        ],
    },
}
