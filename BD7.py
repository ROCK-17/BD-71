import marshal,zlib,base64
exec(marshal.loads(zlib.decompress(base64.b64decode("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"))))