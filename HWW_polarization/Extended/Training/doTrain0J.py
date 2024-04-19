import ROOT
import uproot
import pandas as pd
import numpy as np
import subprocess
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import roc_curve, auc
from sklearn import metrics
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import classification_report, roc_auc_score

import random
import xgboost as xgb
import pandas as pd
import numpy as np

# Modelling
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score, ConfusionMatrixDisplay
from sklearn.model_selection import RandomizedSearchCV, train_test_split
from scipy.stats import randint
from sklearn.datasets import make_classification

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import roc_curve, auc

from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.metrics import classification_report, roc_auc_score

import matplotlib.pyplot as plt

ROOT.EnableImplicitMT()

var = ['mll',
       'mth',
       'mtw1',
       'mtw2',
       'ptll',
       'drll',
       'dphilmet1',
       'dphilmet2',
       'dphill',
       'PuppiMET_pt',
       'PuppiMET_phi',
       'detall',
       'mpmet',
       'dphillmet',
       'dphilljet',
       'dphijet1met',
       'uperp',
       'upara',
       'TkMET_pt',
       'MET_pt',
       'projtkmet',
       'projpfmet',
       'PfMetDivSumMet',
       'recoil',
       'jetpt',
       'PV_npvsGood'
       ]

dir2016 = '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/Summer16_102X_nAODv7_Full2016v7/MCl1loose2016v7__MCCorr2016v7__l2loose__l2tightOR2016v7'
dir2017 = '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/Fall2017_102X_nAODv7_Full2017v7/MCl1loose2017v7__MCCorr2017v7__l2loose__l2tightOR2017v7'
dir2018 = '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/Autumn18_102X_nAODv7_Full2018v7/MCl1loose2018v7__MCCorr2018v7__l2loose__l2tightOR2018v7'


##### GGH                                                                                                                                                          

#names_2016 = ["nanoLatino_GluGluHToWWTo2L2Nu_M125__part*"]
#names_2017 = ["nanoLatino_GluGluHToWWTo2L2Nu_M125__part*"]
#names_2018 = ["nanoLatino_GluGluHToWWTo2L2Nu_M125__part*"]

names_2016 = ["nanoLatino_GluGluHToWWTo2L2Nu_M125__part*", "nanoLatino_GluGluHToWWTo2L2NuAMCNLO_M125__part*", "nanoLatino_GluGluHToWWTo2L2NuPowheg_M125__part*", "nanoLatino_GluGluHToWWTo2L2Nu_M125_herwigpp__part*","nanoLatino_GluGluHToWWTo2L2Nu_alternative_M125__part*", "nanoLatino_GGHjjToWWTo2L2Nu_minloHJJ_M125__part*"]
names_2017 = ["nanoLatino_GluGluHToWWTo2L2Nu_M125__part*", "nanoLatino_GluGluHToWWTo2L2NuPowheg_M125__part*", "nanoLatino_GluGluHToWWTo2L2NuPowhegNNLOPS_M125__part*", "nanoLatino_GGHjjToWWTo2L2Nu_minloHJJ_M125__part*"]
names_2018 = ["nanoLatino_GluGluHToWWTo2L2Nu_M125__part*", "nanoLatino_GluGluHToWWTo2L2NuPowheg_M125__part*", "nanoLatino_GluGluHToWWTo2L2NuPowhegNNLOPS_M125__part*", "nanoLatino_GGHjjToWWTo2L2Nu_minloHJJ_M125__part*"]

fnames_2016 = []
for name in names_2016:
  cmd = ("find {} -name '"+name+"'").format(dir2016)
  fnames_2016_tmp = subprocess.check_output(cmd, shell=True).strip().split(b'\n')
  fnames_2016_tmp = [fname_2016_tmp.decode('ascii') for fname_2016_tmp in fnames_2016_tmp]
  fnames_2016 = fnames_2016_tmp


fnames_2017 = []
for name in names_2017:
    cmd = ("find {} -name '"+name+"'").format(dir2017)
    fnames_2017_tmp = subprocess.check_output(cmd, shell=True).strip().split(b'\n')
    fnames_2017_tmp = [fname_2017_tmp.decode('ascii') for fname_2017_tmp in fnames_2017_tmp]
    fnames_2017 = fnames_2017_tmp

fnames_2018 = []
for name in names_2018:
    cmd = ("find {} -name '"+name+"'").format(dir2018)
    fnames_2018_tmp = subprocess.check_output(cmd, shell=True).strip().split(b'\n')
    fnames_2018_tmp = [fname_2018_tmp.decode('ascii') for fname_2018_tmp in fnames_2018_tmp]
    fnames_2018 = fnames_2018_tmp

    
input_signal = []
for i in fnames_2016[0:]:
    input_signal.append(i)

for i in fnames_2017[0:]:
    input_signal.append(i)

for i in fnames_2018[0:]:
    input_signal.append(i)



names_2016 = ['nanoLatino_WWTo2L2NuHerwigPS__part*', 'nanoLatino_WWTo2L2Nu_DoubleScattering__part', 'nanoLatino_WWTo2L2Nu__part*']
names_2017 = ['nanoLatino_WWTo2L2Nu_DoubleScattering__part', 'nanoLatino_WWTo2L2Nu__part*']
names_2018 = ['nanoLatino_WWTo2L2Nu_DoubleScattering__part', 'nanoLatino_WWTo2L2Nu__part*']


fnames_2016 = []
for name in names_2016:
    cmd = ("find {} -name '"+name+"'").format(dir2016)
    fnames_2016_tmp = subprocess.check_output(cmd, shell=True).strip().split(b'\n')
    fnames_2016_tmp = [fname_2016_tmp.decode('ascii') for fname_2016_tmp in fnames_2016_tmp]
    fnames_2016 = fnames_2016_tmp

fnames_2017 = []
for name in names_2017:
    cmd = ("find {} -name '"+name+"'").format(dir2017)
    fnames_2017_tmp = subprocess.check_output(cmd, shell=True).strip().split(b'\n')
    fnames_2017_tmp = [fname_2017_tmp.decode('ascii') for fname_2017_tmp in fnames_2017_tmp]
    fnames_2017 = fnames_2017_tmp

fnames_2018 = []
for name in names_2018:
    cmd = ("find {} -name '"+name+"'").format(dir2018)
    fnames_2018_tmp = subprocess.check_output(cmd, shell=True).strip().split(b'\n')
    fnames_2018_tmp = [fname_2018_tmp.decode('ascii') for fname_2018_tmp in fnames_2018_tmp]
    fnames_2018 = fnames_2018_tmp


input_bkg = []

for i in fnames_2016:
    input_bkg.append(i)

for i in fnames_2017:
    input_bkg.append(i)

for i in fnames_2018:
    input_bkg.append(i)
    
    
names_2016 = ['nanoLatino_TTTo2L2Nu__part*', 'nanoLatino_ST_s-channel__part*', 'nanoLatino_ST_t-channel_antitop__part*', 'nanoLatino_ST_t-channel_top__part*', 'nanoLatino_ST_tW_antitop__part*', 'nanoLatino_ST_tW_top__part*']
names_2017 = ['nanoLatino_TTTo2L2Nu_PSWeights__part*', 'nanoLatino_ST_s-channel__part*', 'nanoLatino_ST_t-channel_antitop__part*', 'nanoLatino_ST_t-channel_top__part*', 'nanoLatino_ST_tW_antitop__part*', 'nanoLatino_ST_tW_top__part*']
names_2018 = ['nanoLatino_TTTo2L2Nu__part*', 'nanoLatino_ST_s-channel_ext1__part*', 'nanoLatino_ST_t-channel_antitop__part*', 'nanoLatino_ST_t-channel_top__part*', 'nanoLatino_ST_tW_antitop_ext1__part*', 'nanoLatino_ST_tW_top_ext1__part*']


fnames_2016 = []
for name in names_2016:
    cmd = ("find {} -name '"+name+"'").format(dir2016)
    fnames_2016_tmp = subprocess.check_output(cmd, shell=True).strip().split(b'\n')
    fnames_2016_tmp = [fname_2016_tmp.decode('ascii') for fname_2016_tmp in fnames_2016_tmp]
    fnames_2016 = fnames_2016 + fnames_2016_tmp

fnames_2017 = []
for name in names_2017:
    cmd = ("find {} -name '"+name+"'").format(dir2017)
    fnames_2017_tmp = subprocess.check_output(cmd, shell=True).strip().split(b'\n')
    fnames_2017_tmp = [fname_2017_tmp.decode('ascii') for fname_2017_tmp in fnames_2017_tmp]
    fnames_2017 = fnames_2017 + fnames_2017_tmp

fnames_2018 = []
for name in names_2018:
    cmd = ("find {} -name '"+name+"'").format(dir2018)
    fnames_2018_tmp = subprocess.check_output(cmd, shell=True).strip().split(b'\n')
    fnames_2018_tmp = [fname_2018_tmp.decode('ascii') for fname_2018_tmp in fnames_2018_tmp]
    fnames_2018 = fnames_2018 + fnames_2018_tmp

for i in fnames_2016:
    input_bkg.append(i)

for i in fnames_2017:
    input_bkg.append(i)

for i in fnames_2018:
    input_bkg.append(i)

#names_2016 = ['nanoLatino_DYJetsToTT_MuEle_M-50_ext1__part*', 'nanoLatino_DYJetsToLL_M-10to50-LO__part*']
#names_2017 = ['nanoLatino_DYJetsToTT_MuEle_M-50__part*', 'nanoLatino_DYJetsToLL_M-10to50-LO_ext1__part*']
#names_2018 = ['nanoLatino_DYJetsToTT_MuEle_M-50__part*', 'nanoLatino_DYJetsToLL_M-10to50-LO_ext1__part*']

names_2016 = ['nanoLatino_DYJetsToLL_M-50__part*', 'nanoLatino_DYJetsToLL_M-10to50-LO__part*']
names_2017 = ['nanoLatino_DYJetsToLL_M-50__part*', 'nanoLatino_DYJetsToLL_M-10to50-LO_ext1__part*']
names_2018 = ['nanoLatino_DYJetsToLL_M-50__part*', 'nanoLatino_DYJetsToLL_M-10to50-LO_ext1__part*']

fnames_2016 = []
for name in names_2016:
    cmd = ("find {} -name '"+name+"'").format(dir2016)
    fnames_2016_tmp = subprocess.check_output(cmd, shell=True).strip().split(b'\n')
    fnames_2016_tmp = [fname_2016_tmp.decode('ascii') for fname_2016_tmp in fnames_2016_tmp]
    fnames_2016 = fnames_2016 + fnames_2016_tmp


fnames_2017 = []
for name in names_2017:
    cmd = ("find {} -name '"+name+"'").format(dir2017)
    fnames_2017_tmp = subprocess.check_output(cmd, shell=True).strip().split(b'\n')
    fnames_2017_tmp = [fname_2017_tmp.decode('ascii') for fname_2017_tmp in fnames_2017_tmp]
    fnames_2017 = fnames_2017 + fnames_2017_tmp

fnames_2018 = []
for name in names_2018:
    cmd = ("find {} -name '"+name+"'").format(dir2018)
    fnames_2018_tmp = subprocess.check_output(cmd, shell=True).strip().split(b'\n')
    fnames_2018_tmp = [fname_2018_tmp.decode('ascii') for fname_2018_tmp in fnames_2018_tmp]
    fnames_2018 = fnames_2018 + fnames_2018_tmp

for i in fnames_2016:
    input_bkg.append(i)

for i in fnames_2017:
    input_bkg.append(i)

for i in fnames_2018:
    input_bkg.append(i)




df_signal = ROOT.RDataFrame("Events", input_signal)
df_bkg = ROOT.RDataFrame("Events", input_bkg)
df = ROOT.RDataFrame("Events", input_signal)


ROOT.gInterpreter.Declare(
    """
    #include "TSystem.h"
    #include "iostream"
    #include "vector"
    #include "TLorentzVector.h"
    #include "TMath.h"
    #include "TSystem.h"
    #include <map>
    #include "TString.h"
    
    #include "Math/Point3D.h"
    #include "Math/Vector3D.h"
    #include "Math/Vector4D.h"
    #include "Math/Rotation3D.h"
    #include "Math/EulerAngles.h"
    #include "Math/AxisAngle.h"
    #include "Math/Quaternion.h"
    #include "Math/RotationX.h"
    #include "Math/RotationY.h"
    #include "Math/RotationZ.h"
    #include "Math/RotationZYX.h"
    #include "Math/LorentzRotation.h"
    #include "Math/Boost.h"
    #include "Math/BoostX.h"
    #include "Math/BoostY.h"
    #include "Math/BoostZ.h"
    #include "Math/Transform3D.h"
    #include "Math/Plane3D.h"
    #include "Math/VectorUtil.h"
    #include "TMatrixD.h"
    #include "TVectorD.h"
    #include "TMath.h"
    
    
    Double_t MW = 80.3579736098775;
    Double_t WW = 2.084298998278219;
    Double_t s2w = 0.22283820939806098;
    Double_t c2w = 0.777161790601939;
    Double_t cL= 4.0*sqrt(c2w/2.0);
    Double_t cR = 0.0;
    
    Double_t GF = ROOT::Math::sqrt(2)/(2*246*246);
    Double_t gW = ROOT::Math::sqrt((GF/ROOT::Math::sqrt(2)) * 8 * MW*MW);
    Double_t ghWW = gW*MW;
    
    
    TVector3 rotinv(TVector3 p, TVector3 q){
    
      TVector3 pp(0.0, 0.0, 0.0);
    
      double qmodt = q.X()*q.X()+q.Y()*q.Y();
      double qmod = qmodt + q.Z()*q.Z();
      qmodt = TMath::Sqrt(qmodt);
      qmod = TMath::Sqrt(qmod);
    
      if (qmod==0.0){
        cout << "Error while rotation" << endl;
        return pp;
      }
    
      double cth = q.Z() / qmod;
      double sth = 1.0 - cth*cth;
    
      if (sth==0.0){
        pp = p;
        return pp;
      }
    
      sth = TMath::Sqrt(sth);
    
      if (qmodt==0.0){
        pp = p;
        return pp;
      }
    
      double cfi = q.X() / qmodt;
      double sfi = q.Y() / qmodt;
    
      double p1 = p.X();
      double p2 = p.Y();
      double p3 = p.Z();
    
      double pp1 = cth*cfi*p1+cth*sfi*p2-sth*p3;
      double pp2 = -sfi*p1+cfi*p2;
      double pp3 = sth*cfi*p1+sth*sfi*p2+cth*p3;
    
      pp.SetXYZ(pp1, pp2, pp3);
      return pp;
    }

    
    TLorentzVector boostinv(TLorentzVector q, TLorentzVector pboost){
    
      TLorentzVector qprime(0.0, 0.0, 0.0, 0.0);
    
      double rmboost = pboost.E()*pboost.E() - pboost.X()*pboost.X() - pboost.Y()*pboost.Y() - pboost.Z()*pboost.Z();
      if (rmboost>0.0){
        rmboost = TMath::Sqrt(rmboost);
      }else{
        rmboost = 0.0;
      }
    
      double aux = (q.E()*pboost.E() - q.X()*pboost.X() - q.Y()*pboost.Y() - q.Z()*pboost.Z()) / rmboost ;
      double aaux = (aux+q.E()) / (pboost.E()+rmboost);
    
      double qprimeE = aux;
      double qprimeX = q.X() - aaux*pboost.X();
      double qprimeY = q.Y() - aaux*pboost.Y();
      double qprimeZ = q.Z() - aaux*pboost.Z();
    
      qprime.SetPxPyPzE(qprimeX, qprimeY, qprimeZ, qprimeE);
    
      return qprime;
    }
    
        
    Double_t distTheta00(Double_t costheta, Double_t costheta1){
    
      Double_t distTheta00_ = 16.0*(cR*cR*cR*cR + 2*cL*cL*cR*cR + cL*cL*cL*cL)*(1.0 - costheta*costheta)*(1.0 - costheta1*costheta1);
      return distTheta00_;
    }
    
    Double_t distThetaLL(Double_t costheta, Double_t costheta1){
    
      Double_t distThetaLL_ = 4.0*(cR*cR*cR*cR*(1.0 + costheta)*(1.0 + costheta)*(1.0 + costheta1)*(1.0 + costheta1) + cL*cL*cR*cR*((1.0 + costheta)*(1.0 + costheta)*(1.0 - costheta1)*(1.0 - costheta1) + (1.0 - costheta)*(1.0 - costheta)*(1.0 + costheta1)*(1.0 + costheta1)\
    ) + cL*cL*cL*cL*(1.0 - costheta)*(1.0 - costheta)*(1.0 - costheta1)*(1.0 - costheta1));
      return distThetaLL_;
    }
    
    Double_t distThetaRR(Double_t costheta, Double_t costheta1){
    
      Double_t distThetaRR_ = 4.0*(cR*cR*cR*cR*(1.0 - costheta)*(1.0 - costheta)*(1.0 - costheta1)*(1.0 - costheta1) + cL*cL*cR*cR*((1.0 + costheta)*(1.0 + costheta)*(1.0 - costheta1)*(1.0 - costheta1) + (1.0 - costheta)*(1.0 - costheta)*(1.0 + costheta1)*(1.0 + costheta1)\
    ) + cL*cL*cL*cL*(1.0 + costheta)*(1.0 + costheta)*(1.0 + costheta1)*(1.0 + costheta1));
      return distThetaRR_;
    }
    
    Double_t distTheta0L(Double_t costheta, Double_t costheta1, Double_t cosphi){
    
      Double_t sintheta = TMath::Sqrt(1.0-costheta*costheta);
      Double_t sintheta1 = TMath::Sqrt(1.0-costheta1*costheta1);
    
      Double_t disTheta0L_ = -16.0*( cR*cR*cR*cR*(1.0 + costheta)*(1.0 + costheta1) + cL*cL*cL*cL*(1.0 - costheta)*(1.0 - costheta1) - cL*cL*cR*cR*( (1.0 + costheta)*(1.0 - costheta1) + (1.0-costheta)*(1.0+costheta1)))*sintheta*sintheta1*cosphi;
    
      return disTheta0L_;
    }
    
    Double_t distTheta0R(Double_t costheta, Double_t costheta1, Double_t cosphi){
    
      Double_t sintheta = TMath::Sqrt(1.0-costheta*costheta);
      Double_t sintheta1 = TMath::Sqrt(1.0-costheta1*costheta1);
    
      Double_t disTheta0R_ =-16.0*( cR*cR*cR*cR*(1.0 - costheta)*(1.0 - costheta1) + cL*cL*cL*cL*(1.0 + costheta)*(1.0 + costheta1) - cL*cL*cR*cR*( (1.0 + costheta)*(1.0 - costheta1) + (1.0-costheta)*(1.0+costheta1)))*sintheta*sintheta1*cosphi;
    
      return disTheta0R_;
    }
    
    Double_t distThetaLR(Double_t costheta, Double_t costheta1, Double_t cosphi){
    
      Double_t sintheta = TMath::Sqrt(1.0-costheta*costheta);
      Double_t sintheta1 = TMath::Sqrt(1.0-costheta1*costheta1);
      Double_t cos2phi = 2.0*cosphi*cosphi -1.0;
    
      Double_t disThetaLR_ = 8.0*(cL*cL + cR*cR)*(cL*cL + cR*cR)*sintheta*sintheta*sintheta1*sintheta1*cos2phi;
      return disThetaLR_;
    }

    


    ROOT::RVecF ME_weights(ROOT::RVecF GenPart_pt, ROOT::RVecF GenPart_eta, ROOT::RVecF GenPart_phi, ROOT::RVecF GenPart_mass, ROOT::RVecI GenPart_pdgId, ROOT::RVecF GenPart_status, ROOT::RVecI GenPart_genPartIdxMother){
        
        ROOT::Math::PtEtaPhiEVector genWp;
        ROOT::Math::PtEtaPhiEVector genWm;
        ROOT::Math::PtEtaPhiEVector genlp;
        ROOT::Math::PtEtaPhiEVector genlm;
        ROOT::Math::PtEtaPhiEVector gennup;
        ROOT::Math::PtEtaPhiEVector gennum;
        ROOT::Math::PtEtaPhiEVector genH;
        TLorentzVector vector_lp;
        TLorentzVector vector_lm;
        TLorentzVector vector_nup;
        TLorentzVector vector_num;
        TLorentzVector vector_Wp;
        TLorentzVector vector_Wm;
    
        TLorentzVector WP;
        TLorentzVector WM;
        TLorentzVector H;
    
    
        Int_t number_elec = 0;
        Int_t number_muon = 0;
        Int_t number_tau = 0;
    
        Int_t pos_wp = 999;
        Int_t pos_wm = 999;
    
        Int_t mother_pos = 0;
    
        unsigned int nGen = GenPart_pt.size();

        for (unsigned int p = 0; p < nGen; p++){

            // Leptons                                                                                                                                                                                                                                                                
        
            mother_pos = GenPart_genPartIdxMother[p];
            if (GenPart_pdgId[p]==11 && GenPart_pdgId[mother_pos]==-24 && GenPart_pdgId[GenPart_genPartIdxMother[mother_pos]]!=15){
        
                pos_wm = mother_pos;
                number_elec++;
                vector_lm.SetPtEtaPhiM(GenPart_pt[p], GenPart_eta[p], GenPart_phi[p], 0.0);
                genlm.SetCoordinates(GenPart_pt[p], GenPart_eta[p], GenPart_phi[p], vector_lm.E());
        
            }else if (GenPart_pdgId[p]==-11 && GenPart_pdgId[mother_pos]==24 && GenPart_pdgId[GenPart_genPartIdxMother[mother_pos]]!=-15){
        
                pos_wp = mother_pos;
                number_elec++;
                vector_lp.SetPtEtaPhiM(GenPart_pt[p], GenPart_eta[p], GenPart_phi[p], 0.0);
                genlp.SetCoordinates(GenPart_pt[p], GenPart_eta[p], GenPart_phi[p], vector_lp.E());
        
            }else if (GenPart_pdgId[p]==13 && GenPart_pdgId[mother_pos]==-24 && GenPart_pdgId[GenPart_genPartIdxMother[mother_pos]]!=15){
        
                pos_wm = mother_pos;
                number_muon++;
                vector_lm.SetPtEtaPhiM(GenPart_pt[p], GenPart_eta[p], GenPart_phi[p], 0.0);
                genlm.SetCoordinates(GenPart_pt[p], GenPart_eta[p], GenPart_phi[p], vector_lm.E());
        
            }else if (GenPart_pdgId[p]==-13 && GenPart_pdgId[mother_pos]==24 && GenPart_pdgId[GenPart_genPartIdxMother[mother_pos]]!=-15){
        
                pos_wp = mother_pos;
                number_muon++;
                vector_lp.SetPtEtaPhiM(GenPart_pt[p], GenPart_eta[p], GenPart_phi[p], 0.0);
                genlp.SetCoordinates(GenPart_pt[p], GenPart_eta[p], GenPart_phi[p], vector_lp.E());
        
            }else if (GenPart_pdgId[p]==15 && GenPart_pdgId[mother_pos]==-24){
        
                pos_wm = mother_pos;
                number_tau++;
                vector_lm.SetPtEtaPhiM(GenPart_pt[p], GenPart_eta[p], GenPart_phi[p], 0.0);
                genlm.SetCoordinates(GenPart_pt[p], GenPart_eta[p], GenPart_phi[p], vector_lm.E());
        
            }else if (GenPart_pdgId[p]==-15 && GenPart_pdgId[mother_pos]==24){
        
                pos_wp = mother_pos;
                number_tau++;
                vector_lp.SetPtEtaPhiM(GenPart_pt[p], GenPart_eta[p], GenPart_phi[p], 0.0);
                genlp.SetCoordinates(GenPart_pt[p], GenPart_eta[p], GenPart_phi[p], vector_lp.E());
        
            }
                
            if (GenPart_pdgId[p]==-12 && GenPart_pdgId[mother_pos]==-24 && GenPart_pdgId[GenPart_genPartIdxMother[mother_pos]]!=15){
        
              vector_num.SetPtEtaPhiM(GenPart_pt[p], GenPart_eta[p], GenPart_phi[p], 0.0);
              gennum.SetCoordinates(GenPart_pt[p], GenPart_eta[p], GenPart_phi[p], vector_num.E());
              
            }else if (GenPart_pdgId[p]==12 && GenPart_pdgId[mother_pos]==24 && GenPart_pdgId[GenPart_genPartIdxMother[mother_pos]]!=-15){
        
              vector_nup.SetPtEtaPhiM(GenPart_pt[p], GenPart_eta[p], GenPart_phi[p], 0.0);
              gennup.SetCoordinates(GenPart_pt[p], GenPart_eta[p], GenPart_phi[p], vector_nup.E());
        
            }else if (GenPart_pdgId[p]==-14 && GenPart_pdgId[mother_pos]==-24 && GenPart_pdgId[GenPart_genPartIdxMother[mother_pos]]!=15){
        
              vector_num.SetPtEtaPhiM(GenPart_pt[p], GenPart_eta[p], GenPart_phi[p], 0.0);
              gennum.SetCoordinates(GenPart_pt[p], GenPart_eta[p], GenPart_phi[p], vector_num.E());
        
        
            }else if (GenPart_pdgId[p]==14 && GenPart_pdgId[mother_pos]==24 && GenPart_pdgId[GenPart_genPartIdxMother[mother_pos]]!=-15){
        
              vector_nup.SetPtEtaPhiM(GenPart_pt[p], GenPart_eta[p], GenPart_phi[p], 0.0);
              gennup.SetCoordinates(GenPart_pt[p], GenPart_eta[p], GenPart_phi[p], vector_nup.E());
        
            }else if (GenPart_pdgId[p]==-16 && GenPart_pdgId[mother_pos]==-24){
        
              vector_num.SetPtEtaPhiM(GenPart_pt[p], GenPart_eta[p], GenPart_phi[p], 0.0);
              gennum.SetCoordinates(GenPart_pt[p], GenPart_eta[p], GenPart_phi[p], vector_num.E());
        
            }else if (GenPart_pdgId[p]==16 && GenPart_pdgId[mother_pos]==24){
        
              vector_nup.SetPtEtaPhiM(GenPart_pt[p], GenPart_eta[p], GenPart_phi[p], 0.0);
              gennup.SetCoordinates(GenPart_pt[p], GenPart_eta[p], GenPart_phi[p], vector_nup.E());
        
            }

        }
            

        vector_Wp.SetPtEtaPhiM(GenPart_pt[pos_wp], GenPart_eta[pos_wp], GenPart_phi[pos_wp], GenPart_mass[pos_wp]); // W plus                                                                                                                                       
        genWp.SetCoordinates(GenPart_pt[pos_wp], GenPart_eta[pos_wp], GenPart_phi[pos_wp], vector_Wp.E());
    
        vector_Wm.SetPtEtaPhiM(GenPart_pt[pos_wm], GenPart_eta[pos_wm], GenPart_phi[pos_wm], GenPart_mass[pos_wm]); // W minus                                                                                                                                      
        genWm.SetCoordinates(GenPart_pt[pos_wm], GenPart_eta[pos_wm], GenPart_phi[pos_wm], vector_Wm.E());
    
        if ((number_elec+number_muon+number_tau)<2 || pos_wp==999 || pos_wm==999){
            return  ROOT::RVecF(3, -999.9);   
        }

        // Boost over lepton from the Ws reference frame                                                                                                                                                                                                                       
         
        WP = vector_lp + vector_nup;
        WM = vector_lm + vector_num;
        H = WP + WM;
            
        TLorentzVector L11 = vector_lp;
        TLorentzVector L12 = vector_nup;
        TLorentzVector L21 = vector_num;
        TLorentzVector L22 = vector_lm;
                
                
        TLorentzVector L114l = boostinv(L11, H);
        TLorentzVector L124l = boostinv(L12, H);
        TLorentzVector L214l = boostinv(L21, H);
        TLorentzVector L224l = boostinv(L22, H);
    
        TLorentzVector WP4l = boostinv(WP, H);
        TLorentzVector WM4l = boostinv(WM, H);
        TLorentzVector L11V = boostinv(L114l, WP4l);
        TLorentzVector L21V = boostinv(L214l, WM4l);
    
    
        Double_t rmodwp = TMath::Sqrt(WP4l.X()*WP4l.X() + WP4l.Y()*WP4l.Y() + WP4l.Z()*WP4l.Z());
        Double_t rmodwm = TMath::Sqrt(WM4l.X()*WM4l.X() + WM4l.Y()*WM4l.Y() + WM4l.Z()*WM4l.Z());
        Double_t rmod11 = TMath::Sqrt(L11V.X()*L11V.X() + L11V.Y()*L11V.Y() + L11V.Z()*L11V.Z());
        Double_t rmod21 = TMath::Sqrt(L21V.X()*L21V.X() + L21V.Y()*L21V.Y() + L21V.Z()*L21V.Z());
    
        Double_t sprodwp = WP4l.X()*L11V.X() + WP4l.Y()*L11V.Y() + WP4l.Z()*L11V.Z();
        Double_t sprodwm = WM4l.X()*L21V.X() + WM4l.Y()*L21V.Y() + WM4l.Z()*L21V.Z();
    
        Double_t costhetawp = sprodwp / (rmodwp*rmod11);
        Double_t costhetawm = sprodwm / (rmodwm*rmod21);
    
        TVector3 p3wp = WP4l.Vect();
        TVector3 p3wm = WM4l.Vect();
        TVector3 p3l11 = L114l.Vect();
        TVector3 p3l21 = L214l.Vect();
    
                
        TVector3 p3l11R = rotinv(p3l11, p3wp);
        TVector3 p3l21R = rotinv(p3l21, p3wp);
               
        Double_t pt11 = TMath::Sqrt(p3l11R.X()*p3l11R.X() + p3l11R.Y()*p3l11R.Y());
        Double_t pt21 = TMath::Sqrt(p3l21R.X()*p3l21R.X() + p3l21R.Y()*p3l21R.Y());
    
    
        Double_t cosphi = (p3l11R.X()*p3l21R.X() + p3l11R.Y()*p3l21R.Y()) / (pt11*pt21);
        Double_t dphill = TMath::ACos(cosphi);
                
        Double_t Q1 = H.E()*H.E() - H.X()*H.X() - H.Y()*H.Y() - H.Z()*H.Z();
        Double_t Q2 = WP.E()*WP.E() - WP.X()*WP.X() - WP.Y()*WP.Y() - WP.Z()*WP.Z();
        Double_t Q3 = WM.E()*WM.E() - WM.X()*WM.X() - WM.Y()*WM.Y() - WM.Z()*WM.Z();
        Double_t epsfact = (Q1-Q2-Q3)/TMath::Sqrt(Q2*Q3)*0.5;
    
        Double_t K = epsfact;
    
        Double_t ALL2 = epsfact*epsfact * distTheta00(costhetawp, costhetawm);
        Double_t App2 = distThetaLL(costhetawp, costhetawm);
        Double_t Amm2 = distThetaRR(costhetawp, costhetawm);
        Double_t ReALLpp = epsfact*distTheta0L(costhetawp, costhetawm, cosphi);
        Double_t ReALLmm = epsfact*distTheta0R(costhetawp, costhetawm, cosphi);
        Double_t ReAppmm = distThetaLR(costhetawp, costhetawm, cosphi);
    
        Double_t ATT2 = App2 + Amm2 + ReAppmm;
    
        // Final weights                                                                                                                                                                                                                                                            
        Double_t weight_LL = ALL2 / (ALL2 + ATT2 + ReALLpp + ReALLmm);
    
        Double_t weight_TT = ATT2 / (ALL2 + ATT2 + ReALLpp + ReALLmm);
    
        Double_t weight_Int = (ReALLpp + ReALLmm) / (ALL2 + ATT2 + ReALLpp + ReALLmm);
    
        Double_t weight_TTInt = (ATT2 + ReALLpp + ReALLmm) / (ALL2 + ATT2 + ReALLpp + ReALLmm);
    
        Double_t weight_woInt = (ALL2 + ATT2  + ReALLpp + ReALLmm) / (ALL2 + ATT2);

        ROOT::RVecF result(3, 0.0);
        result[0] = (float)weight_LL;
        result[1] = (float)weight_TT;
        result[2] = (float)weight_Int;
        
        return result;
               
    }
    """
)

df = df.Define(
    "ME_weights",
    "ME_weights(GenPart_pt, GenPart_eta, GenPart_phi, GenPart_mass, GenPart_pdgId, GenPart_status, GenPart_genPartIdxMother)"
)

df = df.Define(
    "Higgs_WW_LL",
    "ME_weights[0]"
)
df = df.Define(
    "Higgs_WW_TT",
    "ME_weights[1]"
)
df = df.Define(
    "Higgs_WW_Int",
    "ME_weights[2]"
)

ROOT.gROOT.ProcessLine(
    """
    template
    <typename container>
    float Alt(container c, int index, float alt){
        if (index < c.size()) {
            return c[index];
        }
        else{
            return alt;
        }
    }
    """
)

#df = df.Filter("Higgs_WW_LL>0 && Higgs_WW_LL<5 && Higgs_WW_TT>0 && Higgs_WW_TT<5 && Alt(CleanJet_pt, 0, 0)<30. && Sum(CleanJet_pt > 20. && abs(CleanJet_eta) < 2.5 && Take(Jet_btagDeepFlavB, CleanJet_jetIdx) > 0.0532) == 0 && mth>40 && PuppiMET_pt>20 && mll > 12 && mpmet>15")
#df_bkg = df_bkg.Filter("Alt(CleanJet_pt, 0, 0)<30. && Sum(CleanJet_pt > 20. && abs(CleanJet_eta) < 2.5 && Take(Jet_btagDeepFlavB, CleanJet_jetIdx) > 0.0532) == 0 && mth>40 && PuppiMET_pt>20 && mll > 12 && mpmet>15")

df = df.Filter("(Lepton_pdgId[0]*Lepton_pdgId[1] == -11*11 || Lepton_pdgId[0]*Lepton_pdgId[1] == -13*13) && Lepton_pt[0]>25 && Lepton_pt[1]>15 && Alt(Lepton_pt,2, 0)<10 && ptll>15 && mll > 12 && Higgs_WW_LL>0 && Higgs_WW_LL<5 && Higgs_WW_TT>0 && Higgs_WW_TT<5 && Alt(CleanJet_pt, 0, 0)<30. && Sum(CleanJet_pt > 20. && abs(CleanJet_eta) < 2.5 && Take(Jet_btagDeepFlavB, CleanJet_jetIdx) > 0.0532) == 0 && mth>40 && PuppiMET_pt>20 && mll > 12 && mpmet>15")

df_bkg = df_bkg.Filter("(Lepton_pdgId[0]*Lepton_pdgId[1] == -11*11 || Lepton_pdgId[0]*Lepton_pdgId[1] == -13*13) && Lepton_pt[0]>25 && Lepton_pt[1]>15 && Alt(Lepton_pt,2, 0)<10 && ptll>15 && mll > 12 && Alt(CleanJet_pt, 0, 0)<30. && Sum(CleanJet_pt > 20. && abs(CleanJet_eta) < 2.5 && Take(Jet_btagDeepFlavB, CleanJet_jetIdx) > 0.0532) == 0 && mth>40 && PuppiMET_pt>20 && mll > 12 && mpmet>15")

df = df.Define("jetpt", "Alt(CleanJet_pt, 0, 0)")
df_bkg = df_bkg.Define("jetpt", "Alt(CleanJet_pt, 0, 0)")

columns = ["mll", "mth", "mtw1", "mtw2", "mcollWW", "ptll", "pTWW", "Lepton_pt", "Lepton_eta", "Lepton_phi", 
           "dphilmet", "dphilmet1", "dphilmet2", "dphill", "detall", "drll", "mpmet", "PuppiMET_pt", 
           "PuppiMET_phi", "upara", "uperp", "mTi", "mTe", "mT2", "yll", "projpfmet", "projtkmet", "mcoll", "mR", "dphillmet",
           "Higgs_WW_LL", "Higgs_WW_TT", "Higgs_WW_Int",
           'dphillmet',
           'dphilljet',
           'dphijet1met',
           'uperp',
           'upara',
           'TkMET_pt',
           'MET_pt',
           'projtkmet',
           'projpfmet',
           'PfMetDivSumMet',
           'recoil',
           'jetpt',
           'PV_npvsGood']


print("Creating polarized datasets!")

DF_ALL = pd.DataFrame(df.AsNumpy(columns))

print("Original length: " + str(len(DF_ALL)))

DF_LL, DF_TT = train_test_split(DF_ALL, test_size=0.5, random_state=6)

new_indx_LL = random.choices(DF_LL.index, weights=DF_LL['Higgs_WW_LL'].values, k=int(0.6*len(DF_LL)))
new_indx_TT = random.choices(DF_TT.index, weights=DF_TT['Higgs_WW_TT'].values, k=int(0.6*len(DF_TT)))

LL_resampled = DF_LL.loc[new_indx_LL]
TT_resampled = DF_TT.loc[new_indx_TT]

print("Resampled length: " + str(len(LL_resampled) + len(TT_resampled)))

df_ll = ROOT.RDF.FromNumpy({"mll": LL_resampled["mll"].values, 
                            "mth": LL_resampled["mth"].values, 
                            "mtw1": LL_resampled["mtw1"].values, 
                            "mtw2": LL_resampled["mtw2"].values, 
                            "mcollWW": LL_resampled["mcollWW"].values, 
                            "ptll": LL_resampled["ptll"].values, 
                            "pTWW": LL_resampled["pTWW"].values,  
                            "dphilmet1": LL_resampled["dphilmet1"].values, 
                            "dphilmet2": LL_resampled["dphilmet2"].values, 
                            "dphill": LL_resampled["dphill"].values, 
                            "detall": LL_resampled["detall"].values, 
                            "drll": LL_resampled["drll"].values, 
                            "mpmet": LL_resampled["mpmet"].values,
                            "PuppiMET_pt": LL_resampled["PuppiMET_pt"].values,
                            "PuppiMET_phi": LL_resampled["PuppiMET_phi"].values,
                            #
                            "dphillmet": LL_resampled["dphillmet"].values,
                            "dphilljet": LL_resampled["dphilljet"].values,
                            "dphijet1met":	LL_resampled["dphijet1met"].values,
                            "uperp":	LL_resampled["uperp"].values,
                            "upara":	LL_resampled["upara"].values,
                            "TkMET_pt":	LL_resampled["TkMET_pt"].values,
                            "MET_pt":	LL_resampled["MET_pt"].values,
                            "projtkmet":	LL_resampled["projtkmet"].values,
                            "projpfmet":	LL_resampled["projpfmet"].values,
                            "PfMetDivSumMet":	LL_resampled["PfMetDivSumMet"].values,
                            "recoil":	LL_resampled["recoil"].values,
                            "jetpt":	LL_resampled["jetpt"].values,
                            "PV_npvsGood":	LL_resampled["PV_npvsGood"].values}
                          )

df_tt = ROOT.RDF.FromNumpy({"mll": TT_resampled["mll"].values, 
                            "mth": TT_resampled["mth"].values, 
                            "mtw1": TT_resampled["mtw1"].values, 
                            "mtw2": TT_resampled["mtw2"].values, 
                            "mcollWW": TT_resampled["mcollWW"].values, 
                            "ptll": TT_resampled["ptll"].values, 
                            "pTWW": TT_resampled["pTWW"].values, 
                            "dphill": TT_resampled["dphill"].values, 
                            "detall": TT_resampled["detall"].values, 
                            "drll": TT_resampled["drll"].values, 
                            "mpmet": TT_resampled["mpmet"].values,
                            "dphilmet": TT_resampled["dphilmet"].values,
                            "dphilmet1": TT_resampled["dphilmet1"].values, 
                            "dphilmet2": TT_resampled["dphilmet2"].values,
                            "PuppiMET_pt": TT_resampled["PuppiMET_pt"].values,
                            "PuppiMET_phi": TT_resampled["PuppiMET_phi"].values,
                            #
                            "dphillmet": TT_resampled["dphillmet"].values,
                            "dphilljet": TT_resampled["dphilljet"].values,
                            "dphijet1met":      TT_resampled["dphijet1met"].values,
                            "uperp":    TT_resampled["uperp"].values,
                            "upara":    TT_resampled["upara"].values,
                            "TkMET_pt": TT_resampled["TkMET_pt"].values,
                            "MET_pt":   TT_resampled["MET_pt"].values,
                            "projtkmet":        TT_resampled["projtkmet"].values,
                            "projpfmet":        TT_resampled["projpfmet"].values,
                            "PfMetDivSumMet":   TT_resampled["PfMetDivSumMet"].values,
                            "recoil":   TT_resampled["recoil"].values,
                            "jetpt":    TT_resampled["jetpt"].values,
                            "PV_npvsGood":      TT_resampled["PV_npvsGood"].values}
                          )


print("DONE!")
print("Create pandas dataframes!")


dfLL = df_ll.AsNumpy(var)
dfTT = df_tt.AsNumpy(var)
dfBkg = df_bkg.AsNumpy(var)

dfTot = pd.DataFrame(df.AsNumpy(var))

LL = pd.DataFrame(dfLL)
TT = pd.DataFrame(dfTT)
Bkg = pd.DataFrame(dfBkg)

print("Length signal: " + str(len(LL) + len(TT)))
print("Length Background: " + str(len(Bkg)))

#### Categories!
LL['isLL'] = np.ones(len(LL))
TT['isLL'] = np.zeros(len(TT))
Bkg['isLL'] = np.zeros(len(Bkg))

LL['isTT'] = np.zeros(len(LL))
TT['isTT'] = np.ones(len(TT))
Bkg['isTT'] = np.zeros(len(Bkg))

LL['isBkg'] = np.zeros(len(LL))
TT['isBkg'] = np.zeros(len(TT))

Bkg['isBkg'] = np.zeros(len(Bkg))
dfTot['isBkg'] = np.ones(len(dfTot))

#df_all = pd.concat([LL,TT,Bkg])
df_all = pd.concat([dfTot, Bkg])

#X_train, X_test, Y_train, Y_test = train_test_split(df_all[var], df_all[['isLL', 'isTT', 'isBkg']], test_size=0.2, random_state=6)
X_train, X_test, Y_train, Y_test = train_test_split(df_all[var], df_all[['isBkg']], test_size=0.2, random_state=6)

print("DONE!")
print("Start training the Random Forest!")

rfc = RandomForestClassifier(n_estimators=1200, max_depth=20, random_state=0)
rfc.fit(X_train, Y_train)

#rfc = xgb.XGBClassifier(n_estimators=300, max_depth=20)
#rfc.fit(X_train, Y_train)

print("DONE!")
print("Save and plot test distributions")

joblib.dump(rfc, 'random_forest_Categorical_Bkg_ss.pkl')

y_pred = rfc.predict_proba(X_test)

discriminant = np.squeeze(np.asarray(y_pred[:, 1]))
true_labels = np.squeeze(np.asarray(Y_test['isBkg']))

discriminant0 = discriminant[list(true_labels == 0)]
discriminant1 = discriminant[list(true_labels == 1)]

binning = np.linspace(0, 1, 51) 

plt.clf()
plt.figure(num=None, figsize=(6, 6))
plt.subplot(111)
pdf0, bins0, patches0 = plt.hist(discriminant0, bins = binning, color = 'r', alpha = 0.3, histtype = 'stepfilled', linewidth = 1, edgecolor='r', label = 'Background')
pdf1, bins1, patches1 = plt.hist(discriminant1, bins = binning, color = 'b', alpha = 0.3, histtype = 'stepfilled', linewidth = 1, edgecolor='b', label = 'H to WW')
plt.legend(loc = 'upper center')
plt.ylabel('Entries', fontsize = 12)
plt.xlabel('Random Forest discriminant', fontsize = 12)
plt.savefig('Discriminant_distribution_0j_Bkg_ss.png', dpi = 600)


plt.clf()
plt.figure(num=None, figsize=(6, 6))
plt.subplot(111)
pdf0, bins0, patches0 = plt.hist(discriminant0, bins = binning, color = 'r', alpha = 0.3, histtype = 'stepfilled', linewidth = 1, edgecolor='r', label = 'Background')
pdf1, bins1, patches1 = plt.hist(discriminant1, bins = binning, color = 'b', alpha = 0.3, histtype = 'stepfilled', linewidth = 1, edgecolor='b', label = 'H to WW')
plt.legend(loc = 'upper center')
plt.yscale('log')
plt.ylabel('Entries', fontsize = 12)
plt.xlabel('Random Forest discriminant', fontsize = 12)
plt.savefig('Log_Discriminant_distribution_0j_Bkg_ss.png', dpi = 600)

fpr, tpr, thresholds = metrics.roc_curve(Y_test["isBkg"], y_pred[:, 1])
auc = metrics.auc(fpr, tpr)

plt.clf()
plt.figure(num=None, figsize=(6, 6))
plt.subplot(111)
plt.plot(fpr, tpr, color = 'r', label = "ROC curve for discriminant")
plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--', label = "Random guess")
plt.legend(loc = "lower right")
plt.xlabel('False Positive rate', fontsize = 12)
plt.ylabel('True Positive rate', fontsize = 12)
plt.savefig('ROC_RandomForest_0j_Bkg_ss.png', dpi = 600)


####
####  Categorical
####

'''

y_pred_B = []
y_pred_L = []
y_pred_T = []

for i in range(len(y_pred)):
  y_pred_B.append(y_pred[i][2])
  y_pred_L.append(y_pred[i][0])
  y_pred_T.append(y_pred[i][1])

#### LL category

discriminant = np.squeeze(np.asarray(y_pred_L))
true_labels = np.squeeze(np.asarray(Y_test['isLL']))

discriminant0 = discriminant[list(true_labels == 0)]
discriminant1 = discriminant[list(true_labels == 1)]

binning = np.linspace(0, 1, 51)

# Plot the discriminant distributions:
plt.clf()
plt.figure(num=None, figsize=(6, 6))
plt.subplot(111)
pdf0, bins0, patches0 = plt.hist(discriminant0, bins = binning, color = 'r', alpha = 0.3, histtype = 'stepfilled', linewidth = 1, edgecolor='r', label = 'TT+Background')
pdf1, bins1, patches1 = plt.hist(discriminant1, bins = binning, color = 'b', alpha = 0.3, histtype = 'stepfilled', linewidth = 1, edgecolor='b', label = 'Higgs to LL')
plt.legend(loc = 'upper center')
plt.ylabel('Entries', fontsize = 12)
plt.xlabel('Random Forest discriminant (LL category)', fontsize = 12)
plt.savefig('Discriminant_distribution_0j_LL_ss.png', dpi = 600)


plt.clf()
plt.figure(num=None, figsize=(6, 6))
plt.subplot(111)
pdf0, bins0, patches0 = plt.hist(discriminant0, bins = binning, color = 'r', alpha = 0.3, histtype = 'stepfilled', linewidth = 1, edgecolor='r', label = 'TT+Background')
pdf1, bins1, patches1 = plt.hist(discriminant1, bins = binning, color = 'b', alpha = 0.3, histtype = 'stepfilled', linewidth = 1, edgecolor='b', label = 'Higgs to LL')
plt.legend(loc = 'upper center')
plt.yscale('log')
plt.ylabel('Entries', fontsize = 12)
plt.xlabel('Random Forest discriminant (LL category)', fontsize = 12)
plt.savefig('Log_Discriminant_distribution_0j_LL_ss.png', dpi = 600)


#discriminant = np.squeeze(np.asarray(y_pred[1][:, 1]))
discriminant = np.squeeze(np.asarray(y_pred_T))
true_labels = np.squeeze(np.asarray(Y_test['isTT']))

discriminant0 = discriminant[list(true_labels == 0)]
discriminant1 = discriminant[list(true_labels == 1)]

plt.clf()
plt.figure(num=None, figsize=(6, 6))
plt.subplot(111)
pdf0, bins0, patches0 = plt.hist(discriminant0, bins = binning, color = 'r', alpha = 0.3, histtype = 'stepfilled', linewidth = 1, edgecolor='r', label = 'LL+Background')
pdf1, bins1, patches1 = plt.hist(discriminant1, bins = binning, color = 'b', alpha = 0.3, histtype = 'stepfilled', linewidth = 1, edgecolor='b', label = 'Higgs to TT')
plt.legend(loc = 'upper center')
plt.ylabel('Entries', fontsize = 12)
plt.xlabel('Random Forest discriminant (TT category)', fontsize = 12)
plt.savefig('Discriminant_distribution_0j_TT_ss.png', dpi = 600)


plt.clf()
plt.figure(num=None, figsize=(6, 6))
plt.subplot(111)
pdf0, bins0, patches0 = plt.hist(discriminant0, bins = binning, color = 'r', alpha = 0.3, histtype = 'stepfilled', linewidth = 1, edgecolor='r', label = 'LL+Background')
pdf1, bins1, patches1 = plt.hist(discriminant1, bins = binning, color = 'b', alpha = 0.3, histtype = 'stepfilled', linewidth = 1, edgecolor='b', label = 'Higgs to TT')
plt.legend(loc = 'upper center')
plt.yscale('log')
plt.ylabel('Entries', fontsize = 12)
plt.xlabel('Random Forest discriminant (TT category)', fontsize = 12)
plt.savefig('Log_Discriminant_distribution_0j_TT_ss.png', dpi = 600)

#discriminant = np.squeeze(np.asarray(y_pred[2][:, 1]))
discriminant = np.squeeze(np.asarray(y_pred_B))
true_labels = np.squeeze(np.asarray(Y_test['isBkg']))

discriminant0 = discriminant[list(true_labels == 0)]
discriminant1 = discriminant[list(true_labels == 1)]


plt.clf()
plt.figure(num=None, figsize=(6, 6))
plt.subplot(111)
pdf0, bins0, patches0 = plt.hist(discriminant0, bins = binning, color = 'r', alpha = 0.3, histtype = 'stepfilled', linewidth = 1, edgecolor='r', label = 'H to WW (LL+TT)')
pdf1, bins1, patches1 = plt.hist(discriminant1, bins = binning, color = 'b', alpha = 0.3, histtype = 'stepfilled', linewidth = 1, edgecolor='b', label = 'Background')
plt.legend(loc = 'upper center')
plt.ylabel('Entries', fontsize = 12)
plt.xlabel('Random Forest discriminant (Bkg category)', fontsize = 12)
plt.savefig('Discriminant_distribution_0j_Bkg_ss.png', dpi = 600)


plt.clf()
plt.figure(num=None, figsize=(6, 6))
plt.subplot(111)
pdf0, bins0, patches0 = plt.hist(discriminant0, bins = binning, color = 'r', alpha = 0.3, histtype = 'stepfilled', linewidth = 1, edgecolor='r', label = 'H to WW (LL+TT)')
pdf1, bins1, patches1 = plt.hist(discriminant1, bins = binning, color = 'b', alpha = 0.3, histtype = 'stepfilled', linewidth = 1, edgecolor='b', label = 'Background')
plt.legend(loc = 'upper center')
plt.yscale('log')
plt.ylabel('Entries', fontsize = 12)
plt.xlabel('Random Forest discriminant (Bkg category)', fontsize = 12)
plt.savefig('Log_Discriminant_distribution_0j_Bkg_ss.png', dpi = 600)


#fpr, tpr, thresholds = metrics.roc_curve(Y_test["isLL"], y_pred[0][:, 1])
#fpr2, tpr2, thresholds2 = metrics.roc_curve(Y_test["isTT"], y_pred[1][:, 1])
#fpr3, tpr3, thresholds3 = metrics.roc_curve(Y_test["isBkg"], y_pred[2][:, 1])

fpr, tpr, thresholds = metrics.roc_curve(Y_test["isLL"], y_pred_L)
fpr2, tpr2, thresholds2 = metrics.roc_curve(Y_test["isTT"], y_pred_T)
fpr3, tpr3, thresholds3 = metrics.roc_curve(Y_test["isBkg"], y_pred_B)
auc = metrics.auc(fpr, tpr)
auc2 = metrics.auc(fpr2, tpr2)
auc3 = metrics.auc(fpr3, tpr3)

plt.clf()
plt.figure(num=None, figsize=(6, 6))
plt.subplot(111)
plt.plot(fpr, tpr, color = 'r', label = "ROC curve for polarization discriminant (LL)")
plt.plot(fpr2, tpr2, color = 'b', label = "ROC curve for polarization discriminant (TT)")
plt.plot(fpr3, tpr3, color = 'g', label = "ROC curve for polarization discriminant (Bkg)")
plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--', label = "Random guess")
plt.legend(loc = "lower right")
plt.xlabel('False Positive rate', fontsize = 12)
plt.ylabel('True Positive rate', fontsize = 12)
plt.savefig('ROC_RandomForest_0j_ss.png', dpi = 600)
'''
