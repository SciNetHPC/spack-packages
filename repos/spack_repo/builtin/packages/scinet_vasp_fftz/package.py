# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.packages.vasp.package import Vasp

from spack.package import *


class ScinetVaspFftz(Vasp):

    depends_on("aocl-fftz+openmp", when="+openmp ^[virtuals=fftw-api] aocl-fftz")

