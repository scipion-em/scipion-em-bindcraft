# **************************************************************************
# *
# * Authors:     Marta Martinez (mmmtnez@cnb.csic.es)
#                Roberto Marabini (roberto@cnb.csic.es)
# *
# * CNB CSIC
# *
# * This program is free software; you can redistribute it and/or modify
# * it under the terms of the GNU General Public License as published by
# * the Free Software Foundation; either version 3 of the License, or
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
import os
import sys

import pwem
import pyworkflow.utils as pwutils
from scipion.install.funcs import VOID_TGZ
from pwem.constants import MAXIT

from .constants import (BINDCRAFT_ENV_ACTIVATION, conda_env, repo_url, repo_colab,
                       repo_name, BINDCRAFT_PROGRAM, CUDA_VERSION)
                        
__version__ = "0.0.1"
_logo = "icon.png"
_references = ['Pacesa_Nickel_Schellhaas_Schmidt_Pyatova_Kissling_Barendse_Choudhury_Kapoor_Alcaraz-Serna_et al._2025']

GIT_INSTALL_CMD = f"bash install_bindcraft.sh --cuda {CUDA_VERSION} --pkg_manager 'conda'"

class Plugin(pwem.Plugin):

    @classmethod
    def _defineVariables(cls):
        cls._defineVar(BINDCRAFT_ENV_ACTIVATION,
                       cls.getBindCraftActivationCmd())

    @classmethod
    def getCarbonaraCmd(cls):
        cmd = cls.getCondaActivationCmd()
        cmd += f" "
        cmd += cls.getVar(BINDCRAFT_ENV_ACTIVATION)
        cmd += f" && {BINDCRAFT_PROGRAM} "
        return cmd

    @classmethod
    def getEnviron(cls):
        environ = pwutils.Environ(os.environ)
        return environ

    @classmethod
    def getBindCraftActivationCmd(cls):   # getActivationCmd
        return f'conda activate {conda_env}'

    @classmethod
    def getDependencies(cls):
        """ Return a list of dependencies. Include conda if
        activation command was not found. """
        condaActivationCmd = cls.getCondaActivationCmd()
        neededProgs = []
        if not condaActivationCmd:
            neededProgs.append('conda')

        return neededProgs

    # @classmethod
    def defineBinaries(cls, env):
        """
        How to install BindCraft package from github in Scipion environment.
        """
        import subprocess
        import json

        def getBindCraftInstallation(version):
            FLAG = f'{conda_env}_{version}_installed'

            conda_env_path = os.environ.get('CONDA_PREFIX', sys.prefix)
            conda_env_path = os.path.dirname(conda_env_path)
            conda_env_path = os.path.join(conda_env_path, conda_env)

            FLAG = os.path.join(conda_env_path, FLAG)
            install_cmds = [
                # Activate Conda y create environment
                f'{cls.getCondaActivationCmd()}'
                f'conda create -y -n {conda_env} python=3.10 && '
                f'conda activate {repo_name} && '
                f'python -m pip install {repo_colab} && '
                f'git clone {repo_url} && '                
                # change to repo_name
                f'cd {repo_name}  && '
                #f'{cls.getBindCraftActivationCmd()} &&'
                # Install
                f'{GIT_INSTALL_CMD} && '
                # Flag installation finished
                f'cd .. && '
                f'touch {FLAG}'
            ]

            # finalCmds = [(" ".join(install_cmds), FLAG)]
            finalCmds = [(install_cmds, FLAG)]

            # BindCraft package registered in Scipion environment
            env.addPackage(
                name="bindcraft",
                version=version,
                tar=VOID_TGZ,  # Only marker
                commands=finalCmds,
                neededProgs=cls.getDependencies(),
                default=True)

        getBindCraftInstallation(version=__version__)

