# Tai Sakuma <tai.sakuma@cern.ch>

##____________________________________________________________________________||
class ReadVersionInfo(object):
    def __call__(self, path):
        file = open(path)
        return self._readImp(file)

    def _readImp(self, file):
        full = file.read()
        # versionInfo.txt is written as
        # https://github.com/CMSRA1/cmg-cmssw-private/blob/RA1cmg_v2.4_patch1/CMGTools/Production/scripts/heppyBatchAlphaT.py#L91
        # the second line will be the tag
        tag = full.split('\n')[1]
        return dict(full = full, tag = tag)

##____________________________________________________________________________||
