# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install aocl-fftz
#
# You can edit this file again by typing:
#
#     spack edit aocl-fftz
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class AoclFftz(CMakePackage):
    """
    AOCL-FFTZ is a high-performance Fast Fourier Transform (FFT) library
    optimized for AMD “Zen”-based CPUs. It efficiently computes FFTs for
    both complex and real data, supporting a wide range of problem sizes
    and dimensions. The library is tuned for both single-threaded and
    multi-threaded execution. AOCL-FFTZ can serve as a drop-in replacement
    for FFTW in applications like VASP (Vienna Ab initio Simulation Package),
    offering a similar API with enhanced functionality.
    """

    homepage = "https://www.amd.com/en/developer/aocl/fftz.html"
    git = "https://github.com/amd/aocl-fftz"
    url = "https://github.com/amd/aocl-fftz/archive/refs/tags/5.2.tar.gz"

    maintainers("amd-toolchain-support")

    license("BSD-3-Clause", checked_by="nolta")

    version("5.2", sha256="7aaf9ae81e20604fd3b59ce4f39f5d97aee2b2c887f9040b69000dcab25c6128")

    variant("openmp", default=True, description="Enable openmp build")

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("fortran", type="build")

    provides("fftw-api@3")

    @property
    def selected_precisions(self):
        return ["float", "double"]

    @property
    def libs(self):
        libraries = ["libfftw3xc_wrapper_fftz"]
        return find_libraries(libraries, root=self.prefix, recursive=True)

    def cmake_args(self):
        instr = "AVX512" if "avx512" in self.spec.target else "AVX256"
        args = [
            self.define("BUILD_THIRD_PARTY_WRAPPERS", True),
            self.define("ENABLE_INSTRUCTIONS_UPTO", instr),
            self.define_from_variant("ENABLE_MULTI_THREADING", "openmp"),
        ]
        return args

