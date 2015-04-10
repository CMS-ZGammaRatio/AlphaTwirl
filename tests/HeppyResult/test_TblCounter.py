from AlphaTwirl.HeppyResult import TblCounter
import unittest
import cStringIO
import collections

##____________________________________________________________________________||
class MockOpen(object):
    def __init__(self, out): self._out = out
    def __call__(self, path): return self._out

##____________________________________________________________________________||
def mockClose(file): pass

##____________________________________________________________________________||
class MockAnalyzer(object):
    def __init__(self, path): self.path = path

##____________________________________________________________________________||
class MockComponent(object):
    def __init__(self, name): self.name = name

##____________________________________________________________________________||
class MockReadCounter(object):
    def __call__(self, path):
        self.path = path
        return self.counter

##____________________________________________________________________________||
class TestTblCounter(unittest.TestCase):

    def test_read(self):
        tblnevt = TblCounter(
            outPath = "t.txt",
            columnNames = ('nevt', 'nevt_sumw'),
            analyzerName = 'skimAnalyzerCount',
            fileName = 'SkimReport.txt',
            levels = ('All Events', 'Sum Weights')
        )

        out = cStringIO.StringIO()
        tblnevt._open = MockOpen(out)
        tblnevt._close = mockClose

        readCounter = MockReadCounter()
        tblnevt._readCounter = readCounter

        tblnevt.begin()

        component = MockComponent("QCD_HT_100To250")
        component.skimAnalyzerCount = MockAnalyzer('201525_SingleMu/QCD_HT_100To250/skimAnalyzerCount')
        readCounter.counter = collections.OrderedDict([('All Events', {'count': 4123612, 'eff2': 1.0, 'eff1': 1.0}), ('Sum Weights', {'count': 4123612.0, 'eff2': 1.0, 'eff1': 1.0})])
        tblnevt.read(component)
        self.assertEqual('201525_SingleMu/QCD_HT_100To250/skimAnalyzerCount/SkimReport.txt', readCounter.path)

        component = MockComponent("TTJets")
        component.skimAnalyzerCount = MockAnalyzer('201525_SingleMu/TTJets/skimAnalyzerCount')
        readCounter.counter = collections.OrderedDict([('All Events', {'count': 25446993, 'eff2': 1.0, 'eff1': 1.0}), ('Sum Weights', {'count': 25446993.0, 'eff2': 1.0, 'eff1': 1.0})])
        tblnevt.read(component)
        self.assertEqual('201525_SingleMu/TTJets/skimAnalyzerCount/SkimReport.txt', readCounter.path)

        component = MockComponent("TBarToLeptons_sch")
        component.skimAnalyzerCount = MockAnalyzer('201525_SingleMu/TBarToLeptons_sch/skimAnalyzerCount')
        readCounter.counter = collections.OrderedDict([('All Events', {'count': 250000, 'eff2': 1.0, 'eff1': 1.0}), ('Sum Weights', {'count': 320855.887262, 'eff2': 1.2834, 'eff1': 1.28})])
        tblnevt.read(component)
        self.assertEqual('201525_SingleMu/TBarToLeptons_sch/skimAnalyzerCount/SkimReport.txt', readCounter.path)

        component = MockComponent("TBarToLeptons_tch")
        component.skimAnalyzerCount = MockAnalyzer('201525_SingleMu/TBarToLeptons_tch/skimAnalyzerCount')
        readCounter.counter = collections.OrderedDict([('All Events', {'count': 1999800, 'eff2': 1.0, 'eff1': 1.0}), ('Sum Weights', {'count': 50734279.1235, 'eff2': 25.3697, 'eff1': 25.37})])
        tblnevt.read(component)
        self.assertEqual('201525_SingleMu/TBarToLeptons_tch/skimAnalyzerCount/SkimReport.txt', readCounter.path)

        tblnevt.end()

        expected = '\n'.join([
            '         component     nevt     nevt_sumw',
            '   QCD_HT_100To250  4123612       4123612',
            '            TTJets 25446993      25446993',
            ' TBarToLeptons_sch   250000 320855.887262',
            ' TBarToLeptons_tch  1999800 50734279.1235']) + '\n'

        self.assertEqual(expected, out.getvalue())


    def test_read_empty(self):
        tblnevt = TblCounter(
            outPath = "t.txt",
            columnNames = ('nevt', 'nevt_sumw'),
            analyzerName = 'skimAnalyzerCount',
            fileName = 'SkimReport.txt',
            levels = ('All Events', 'Sum Weights')
        )

        out = cStringIO.StringIO()
        tblnevt._open = MockOpen(out)
        tblnevt._close = mockClose

        tblnevt.begin()
        tblnevt.end()

        expected = ' component nevt nevt_sumw\n'
        self.assertEqual(expected, out.getvalue())


##____________________________________________________________________________||
