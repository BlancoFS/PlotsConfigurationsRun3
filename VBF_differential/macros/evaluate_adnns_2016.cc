#ifndef ADNN2016
#define ADNN2016

#include <vector>

#include "TVector2.h"
#include "Math/Vector4Dfwd.h"
#include "Math/GenVector/LorentzVector.h"
#include "Math/GenVector/PtEtaPhiM4D.h"

#include "ROOT/RVec.hxx"


#include "generated_code_2_UL_plusDY.h"
#include "generated_code_UL_ggH.h"

using namespace ROOT;
using namespace ROOT::VecOps;


RVecF adversarial_dnn(
        float nLepton,
        float nCleanJet,
        float Lepton_pdgId_1,
        float Lepton_pdgId_2,
        float CleanJet_eta_1,
		float CleanJet_eta_2,
		float CleanJet_phi_1,
		float CleanJet_phi_2,
        float CleanJet_pt_1,
        float CleanJet_pt_2,
        float Lepton_eta_1,
        float Lepton_eta_2,
        float Lepton_phi_1,
        float Lepton_phi_2,
        float Lepton_pt_1,
        float Lepton_pt_2,
        float qgl_1,
        float qgl_2,
        float mjj,
        float mll,
        float ptll,
        float detajj,
        float dphill,
        float PuppiMET_pt,
        float PuppiMET_phi,
        float dphillmet,
        float drll,
        float ht,
        float mTi,
        float mth,  
        float m_l1j1,
        float m_l1j2,
        float m_l2j1,
        float m_l2j2,
        float D_VBF_QCD,
        float D_VBF_VH,
        float D_QCD_VH,
        float D_VBF_DY
        ){
    RVecF adnns;
    adnns.reserve(2);
    
    float input[36];

    input[0] = mjj;
//   Ctot
    input[1] = log((abs(2*Lepton_eta_1-CleanJet_eta_1-CleanJet_eta_2)+abs(2*Lepton_eta_2-CleanJet_eta_1-CleanJet_eta_2))/(detajj));

    input[2] = detajj;
    input[3] = drll;

    input[4] = CleanJet_eta_1;
    input[5] = CleanJet_eta_2;
    input[6] = CleanJet_pt_1;
    input[7] = CleanJet_pt_2;
    input[8] = CleanJet_phi_1;
    input[9] = CleanJet_phi_2;

    input[10] = Lepton_eta_1;
    input[11] = Lepton_eta_2;
    input[12] = Lepton_pt_1;
    input[13] = Lepton_pt_2;
    input[14] = Lepton_phi_1;
    input[15] = Lepton_phi_2;

    input[16] = PuppiMET_pt;
    input[17] = PuppiMET_phi;

    input[18] = mth;
    input[19] = ptll;

    input[20] = m_l1j1;
    input[21] = m_l1j2;
    input[22] = m_l2j1;
    input[23] = m_l2j2;

    input[24] = mll;

    
    input[25] = qgl_1;
    input[26] = qgl_2;

    input[27] = D_VBF_QCD;
    input[28] = D_VBF_VH;
    input[29] = D_QCD_VH;
    input[30] = D_VBF_DY;

    
    input[31] = mTi;
    input[32] = ht;

    input[33] = 1; //y_2016
    input[34] = 0; //y_2017
    input[35] = 0; //y_2018




    adnns.push_back(guess_digit(input, 0));
    adnns.push_back(guess_digit_ggh(input, 0));
    
    return adnns;

}

#endif
  

