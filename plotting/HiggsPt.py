#!/usr/bin/env python3

import ROOT
import matplotlib.pyplot as plt
import argparse
from pathlib import Path
from genericUtils.python.PlotFunctions import *
from genericUtils.python.TAxisFunctions import *


def argument_parse():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--infile", required = True)
    parser.add_argument("-o", "--outdir", default = "plots")
    opts = parser.parse_args()
    return opts


def get_hists_from_keys(infile):
    keys = infile.GetListOfKeys()
    keys = [(key.GetName(), key) for key in keys if (not "RAW" in key.GetName() and not "PDF" in key.GetName() and not "AUX" in key.GetName())]
    return keys


def set_title_and_colour(histograms_names_histos):
    colors = [ROOT.kBlack, ROOT.kRed, ROOT.kBlue]
    for idx, name_hist in enumerate(histograms_names_histos):
        name, hist = name_hist
        name = name.split("/")[-1]
        if name == "pTH":
            name = "Nominal SM"
        else:
            name = name.replace("pTH[", "")[:-1]
            name = name.split("_")
            name[1] = name[1].replace("p", ".").replace("m", "-")
            name = " = ".join(name)
        hist.SetTitle(name)
        hist.GetXaxis().SetTitle("Higgs boson p_{T}")
        hist.GetYaxis().SetTitle("d#sigma/dp_{T}(H) [pb/GeV]")
        hist.SetLineColor(colors[idx])


def plot_one(name, hist, outdir):
    c1 = ROOT.TCanvas()
    hist.Draw("h")
    ROOT.gPad.SetLogy()
    c1.SaveAs(f"{outdir}/{name.split('/')[-1]}.pdf")


def plot_all_overlayed(histograms_names_histos, infile_name, outdir):
    canvas = RatioCanvas("rc", "")
    AddHistogramTop(canvas, histograms_names_histos[0][1], drawopt="HISTE1")
    for name, hist in histograms_names_histos[1:]:
        AddRatio(canvas, hist, histograms_names_histos[0][1], drawopt="HISTE1")
    SetAxisLabels(canvas, "Higgs boson p_{T}", "d#sigma/dp_{T}(H) [pb/GeV]")
    FormatCanvasAxes(canvas)
    DrawText(canvas, GetAtlasInternalText(status='Internal'), 0.6, 0.8, 0.9, 0.9)
    MakeLegend(canvas, 0.6, 0.6, 0.9, 0.8)
    ROOT.gPad.SetLogy()
    canvas.SaveAs(f"{outdir}/{infile_name.split('/')[-1].replace('root', 'pdf')}")


def main():
    # GU setup
    SetupStyle()
    ROOT.gROOT.SetBatch()
    ROOT.gStyle.SetOptStat(0)

    opts = argument_parse()
    Path(opts.outdir).mkdir(parents = True, exist_ok = True)

    infile = ROOT.TFile.Open(opts.infile, "READ")

    histograms_keys = get_hists_from_keys(infile)
    histograms_names_histos = [(hkey[0], hkey[1].ReadObj()) for hkey in histograms_keys]
    histograms_names_histos.sort()

    set_title_and_colour(histograms_names_histos)

    for name, hist in histograms_names_histos:
        plot_one(name, hist, opts.outdir)

    plot_all_overlayed(histograms_names_histos, opts.infile, opts.outdir)

    infile.Close()


if __name__ == '__main__':
    main()
