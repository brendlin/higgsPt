// -*- C++ -*-
#include "Rivet/Analysis.hh"
#include "Rivet/Projections/FinalState.hh"
#include "Rivet/Projections/FastJets.hh"

namespace Rivet {


  class HiggsFullPhaseSpace : public Analysis {
  public:

    /// Default constructor
    HiggsFullPhaseSpace () :
      Analysis("HiggsFullPhaseSpace"){}

    /// Book histograms and initialise projections before the run
    void init() {

      // Histograms with data bins
      const std::vector<double> bins_ptyy = {0, 5, 10, 15, 20, 25, 30, 35, 45, 60, 80, 100, 120, 140, 170, 200, 250, 350, 450, 650, 1000};
      book(_h_pTH, "pTH", bins_ptyy);

      return;
    }


    /// Perform the per-event analysis
    void analyze(const Event& event) {

      const GenEvent* evt = event.genEvent();

      for (HepMC::GenEvent::particle_const_iterator p = evt->particles_begin(); p != evt->particles_end(); ++p) {

         int p_pdg_id = (*p)->pdg_id();

         if (p_pdg_id !=  PID::HIGGSBOSON) continue;
     
         Particle *higgs = new Particle(*p);
  
         const double weight = event.weight();
         // std::cout << "Filling Higgs with pt " << higgs->pT() << std::endl;

         // Note that Pt is in GeV here!
         _h_pTH->fill(higgs->pT(), weight);

       }
    }


    /// Normalise histograms etc., after the run
    void finalize() {
      const double xs = crossSectionPerEvent();
      scale(_h_pTH, xs);
    }


  private:

    Histo1DPtr _h_pTH;

  };


  // The hook for the plugin system
  DECLARE_RIVET_PLUGIN(HiggsFullPhaseSpace);


}
