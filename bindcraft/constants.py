# **************************************************************************
# *
# * Authors:    Marta Martinez (mmmtnez@cnb.csic.es)
# *             Roberto Marabini (roberto@cnb.csic.es) 
# *
# * National Center for Biotechnology (CNB-CSIC)
# *
# * This program is free software; you can redistribute it and/or modify
# * it under the terms of the GNU General Public License as published by
# * the Free Software Foundation; either version 2 of the License, or
# * (at your option) any later version.
# *
# * This program is distributed in the hope that it will be useful,
# * but WITHOUT ANY WARRANTY; without even the implied warranty of
# * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# * GNU General Public License for more details.
# *
# * You should have received a copy of the GNU General Public License
# * along with this program; if not, write to the Free Software
# * Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA
# * 02111-1307  USA
# *
# *  All comments concerning this program package may be sent to the
# *  e-mail address 'scipion@cnb.csic.es'
# *
# **************************************************************************

V1 = "1.5.0"
BINDCRAFT_PROGRAM = 'bindcraft.py'
BINDCRAFT_ENV_ACTIVATION = "BINDCRAFT_ENV_ACTIVATION"
# DEFAULT_ACTIVATION_CMD = "DEFAULT_ACTIVATION_CMD"
repo_url = "https://github.com/martinpacesa/BindCraft "
# string after '@' is the commit hash to be installed
# if this hash is modified the wrapper version should be increased
# GIT_CLONE_CMD = "pip install -vv git+https://github.com/martinpacesa/BindCraft.git@1ed6359f299e14274bd0372bc3fb0594506decc8"
# Git Last commit: 036608554c48e2bfa65c383d514312aaa78fd9bf
repo_colab = "git+https://github.com/sokrypton/ColabDesign.git"
repo_name = "BindCraft"
conda_env = "BindCraft"
CUDA_VERSION = '12.4' # my case in copernico, select the specific one in each case)


CLUSTALO = 'clustalo'

RELAXED_FILTERS = "relaxed_filters.json"
PEPTIDE_RELAXED_FILTERS = "peptide_relaxed_filters.json"
PEPTIDE_FILTERS = "peptide_filters.json"
NO_FILTERS = "no_filters.json"
DEFAULT = "default_filters.json"

SETTING_FILTERS = [
    RELAXED_FILTERS,
    PEPTIDE_RELAXED_FILTERS,
    PEPTIDE_FILTERS,
    NO_FILTERS,
    DEFAULT
]

PEPTIDE_3STAGE_MULTIMER_MPNN = "peptide_3stage_multimer_mpnn.json"
PEPTIDE_3STAGE_MULTIMER_MPNN_FLEXIBLE = "peptide_3stage_multimer_mpnn_flexible.json"
PEPTIDE_3STAGE_MULTIMER = "peptide_3stage_multimer.json"
PEPTIDE_3STAGE_MULTIMER_FLEXIBLE = "peptide_3stage_multimer_flexible.json"
DEFAULT_4STAGE_MULTIMER_MPNN = "default_4stage_multimer_mpnn.json"
DEFAULT_4STAGE_MULTIMER_MPNN_HARDTARGET = "default_4stage_multimer_mpnn_hardtarget.json"
DEFAULT_4STAGE_MULTIMER_MPNN_FLEXIBLE = "default_4stage_multimer_mpnn_flexible.json"
DEFAULT_4STAGE_MULTIMER_MPNN_FLEXIBLE_HARDTARGET = "default_4stage_multimer_mpnn_flexible_hardtarget.json"
DEFAULT_4STAGE_MULTIMER = "default_4stage_multimer.json"
DEFAULT_4STAGE_MULTIMER_HARDTARGET = "default_4stage_multimer_hardtarget.json"
DEFAULT_4STAGE_MULTIMER_FLEXIBLE = "default_4stage_multimer_flexible.json"
DEFAULT_4STAGE_MULTIMER_FLEXIBLE_HARDTARGET = "default_4stage_multimer_flexible_hardtarget.json"
BETASHEET_4STAGE_MULTIMER_MPNN = "betasheet_4stage_multimer_mpnn.json"
BETASHEET_4STAGE_MULTIMER_MPNN_HARDTARGET = "betasheet_4stage_multimer_mpnn_hardtarget.json"
BETASHEET_4STAGE_MULTIMER_MPNN_FLEXIBLE = "betasheet_4stage_multimer_mpnn_flexible.json"
BETASHEET_4STAGE_MULTIMER_MPNN_FLEXIBLE_HARDTARGET = "betasheet_4stage_multimer_mpnn_flexible_hardtarget.json"
BETASHEET_4STAGE_MULTIMER = "betasheet_4stage_multimer.json"
BETASHEET_4STAGE_MULTIMER_HARDTARGET = "betasheet_4stage_multimer_hardtarget.json"
BETASHEET_4STAGE_MULTIMER_FLEXIBLE = "betasheet_4stage_multimer_flexible.json"
BETASHEET_4STAGE_MULTIMER_FLEXIBLE_HARDTARGET = "betasheet_4stage_multimer_flexible_hardtarget.json"


SETTING_ADVANCED = [
    PEPTIDE_3STAGE_MULTIMER_MPNN,
    PEPTIDE_3STAGE_MULTIMER_MPNN_FLEXIBLE,
    PEPTIDE_3STAGE_MULTIMER,
    PEPTIDE_3STAGE_MULTIMER_FLEXIBLE,
    DEFAULT_4STAGE_MULTIMER_MPNN,
    DEFAULT_4STAGE_MULTIMER_MPNN_HARDTARGET,
    DEFAULT_4STAGE_MULTIMER_MPNN_FLEXIBLE,
    DEFAULT_4STAGE_MULTIMER_MPNN_FLEXIBLE_HARDTARGET,
    DEFAULT_4STAGE_MULTIMER,
    DEFAULT_4STAGE_MULTIMER_HARDTARGET,
    DEFAULT_4STAGE_MULTIMER_FLEXIBLE,
    DEFAULT_4STAGE_MULTIMER_FLEXIBLE_HARDTARGET,
    BETASHEET_4STAGE_MULTIMER_MPNN,
    BETASHEET_4STAGE_MULTIMER_MPNN_HARDTARGET,
    BETASHEET_4STAGE_MULTIMER_MPNN_FLEXIBLE,
    BETASHEET_4STAGE_MULTIMER_MPNN_FLEXIBLE_HARDTARGET,
    BETASHEET_4STAGE_MULTIMER,
    BETASHEET_4STAGE_MULTIMER_HARDTARGET,
    BETASHEET_4STAGE_MULTIMER_FLEXIBLE,
    BETASHEET_4STAGE_MULTIMER_FLEXIBLE_HARDTARGET
]

