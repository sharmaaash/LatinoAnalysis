#
#
#     |   |  |  |  / _)        
#     |   |_ |  ' /   |  __ \  
#     |  ___ |  . \   |  |   | 
#    _|      | _|\_\ _| _|  _| 
#                                                         
#
#


from LatinoAnalysis.Gardener.gardening import TreeCloner
import numpy
import ROOT
import math
import sys
import optparse
import re
import warnings
import os.path
from collections import OrderedDict
from array import array;

class L4KinFiller(TreeCloner):
    def __init__(self):
        pass

    def help(self):
        return '''Calculate kinematic variables, event base and not single object based. They are all simple float variables like mll, dphill, ... '''

    def addOptions(self,parser):
        description = self.help()
        group = optparse.OptionGroup(parser,self.label, description)
        group.add_option('-c', '--cmssw', dest='cmssw', help='cmssw version (naming convention may change)', default='805', type='string')
        parser.add_option_group(group)
        return group

    def checkOptions(self,opts):

        self.cmssw = opts.cmssw
        print " cmssw = ", self.cmssw

                    
    def process(self,**kwargs):
        tree  = kwargs['tree']
        input = kwargs['input']
        output = kwargs['output']

        # does that work so easily and give new variable itree and otree?
        self.connect(tree,input)

        nentries = self.itree.GetEntries()
        print 'Total number of entries: ',nentries 
        savedentries = 0

        #
        # create branches for otree, the ones that will be modified!
        # These variables NEED to be defined as functions in ZWWVar.C
        # e.g. mll, dphill, ...
        # if you add a new variable here, be sure it IS defined in ZWWVar.C
        #
        self.namesOldBranchesToBeModifiedSimpleVariable = [
            'lep1Pt',
            'lep2Pt',
            'lep3Pt',
            'lep4Pt',
            'lep1Eta',
            'lep2Eta',
            'lep3Eta',
            'lep4Eta',
            'lep1Phi',
            'lep2Phi',
            'lep3Phi',
            'lep4Phi',
            'pfmet',
            'pfmetPhi',
            'z0mass',
            'z1mass',
            'flagZ1SF',
            'z0DeltaPhi',
            'z1DeltaPhi',
            'z1DeltaR',
            'mllll',
            'chllll',
            'st',
            'njet',
            'nbjet'
            ]
        
        # clone the tree
        self.clone(output, self.namesOldBranchesToBeModifiedSimpleVariable)

        self.oldBranchesToBeModifiedSimpleVariable = {}
        for bname in self.namesOldBranchesToBeModifiedSimpleVariable:
            bvariable = numpy.ones(1, dtype=numpy.float32)
            self.oldBranchesToBeModifiedSimpleVariable[bname] = bvariable

        # now actually connect the branches
        for bname, bvariable in self.oldBranchesToBeModifiedSimpleVariable.iteritems():
            #print " bname   = ", bname
            #print " bvariable = ", bvariable
            self.otree.Branch(bname,bvariable,bname+'/F')

        # input tree and output tree
        itree     = self.itree
        otree     = self.otree


        # change this part into correct path structure... 
        cmssw_base = os.getenv('CMSSW_BASE')
        try:
            ROOT.gROOT.LoadMacro(cmssw_base+'/src/LatinoAnalysis/Gardener/python/variables/ZWWVar.C+g')
        except RuntimeError:
            ROOT.gROOT.LoadMacro(cmssw_base+'/src/LatinoAnalysis/Gardener/python/variables/ZWWVar.C++g')


        #----------------------------------------------------------------------------------------------------
        print '- Starting eventloop'
        step = 5000

        #for i in xrange(2000):
        for i in xrange(nentries):

            itree.GetEntry(i)

            if i > 0 and i%step == 0.:
                print i,'events processed :: ', nentries

            ZWW = ROOT.ZWW()
            ZWW.setLepton(itree.std_vector_lepton_pt, itree.std_vector_lepton_eta, itree.std_vector_lepton_phi, itree.std_vector_lepton_flavour, itree.std_vector_lepton_ch, itree.std_vector_lepton_isTightLepton)
            ZWW.setJet(itree.std_vector_jet_pt, itree.std_vector_jet_eta,itree.std_vector_jet_phi,    itree.std_vector_jet_mass, itree.std_vector_jet_cmvav2)
            
            if self.cmssw == '80x' :

                met = itree.pfType1Met          # formerly pfType1Met
                metphi = itree.pfType1Metphi    # formerly pfType1Metphi
            else :
                met = itree.metPfType1      
                metphi = itree.metPfType1Phi
#                ZWW.setTkMET(itree.metTtrk, itree.metTtrkPhi)
            ZWW.setMET(met, metphi)
 
            ZWW.isAllOk()
            if ZWW.preSelection():
            # now fill the variables like "mll", "dphill", ...
                for bname, bvariable in self.oldBranchesToBeModifiedSimpleVariable.iteritems():
                    bvariable[0] = getattr(ZWW, bname)()
                otree.Fill()
                savedentries+=1

        self.disconnect()
        print '- Eventloop completed'
        print '   Saved: ', savedentries, ' events'
