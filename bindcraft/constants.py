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

repo_name = "BindCraft"
conda_env = "BindCraft"
CUDA_VERSION = '12.4' (# my case in copernico, select the specific one in each case)
CONDA = 'conda'

CLUSTALO = 'clustalo'
