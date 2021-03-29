#!/usr/bin/env python3

import ROOT
import matplotlib.pyplot as plt


def plot_one(infile_name, histname, color):
    infile = ROOT.TFile.Open(infile_name, "READ")
    key = infile.GetKey(histname)
    hist = key.ReadObj()
    hist.SetDirectory(0)
    hist.GetXaxis().SetTitle("Higgs boson p_{T}")
    hist.GetYaxis().SetTitle("a.u.")
    hist.SetLineColor(color)
    hist.Draw("h")
    infile.Close()
    reduced_histname = histname.split("/")[-1]
    reduced_infile = infile_name.split("/")[-1].split(".")[0].replace("Rivet", "")
    plot_name = f"{reduced_histname}_{reduced_infile}"
    return plot_name


def main():
    ROOT.gROOT.SetBatch()
    ROOT.gStyle.SetOptStat(0)

    c1 = ROOT.TCanvas()

    infile_name = "../rivet/Rivet.root"
    h_HpT_name = "/Rivet/HiggsFullPhaseSpace/pTH"
    color = ROOT.kBlue
    plot_name = plot_one(infile_name, h_HpT_name, color)

    c1.SaveAs(f"{plot_name}.pdf")


if __name__ == '__main__':
    main()
