%define _lto_cflags %{nil}

Name:           MusicSpectrum
Version:        0.0.4
Release:        3%{?dist}.nolto
Summary:        Audio spectrum viewer.

License:        CC0-1.0
URL:            https://github.com/lucasfturos/MusicSpectrum.git
Source0:        https://github.com/geraldosimiao/MusicSpectrum/archive/refs/tags/%{version}.tar.gz

BuildRequires:  make
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  git
BuildRequires:  git-core
BuildRequires:  SFML
BuildRequires:  SFML-devel
BuildRequires:  gtkglext-libs
BuildRequires:  gtkglext-devel
BuildRequires:  GLC_lib
BuildRequires:  ninja-build



%description
Audio spectrum viewer. Application of the Fourier transform FFT in conjunction with Euler's formula.
      -Supports audios in WAV format.
      -Developed in C++ and SFML.

%prep
%autosetup 

%build
mkdir build
cd build
cmake ..
make -j4

%install
%cmake_install

%files -f %{name}.lang
%license LICENSES
%doc README.md
%{_bindir}/%{name}


%changelog
* Mon Jan 22 2024 Geraldo Simião <geraldosimiao@fedoraproject.org> - 0.0.4-3
- Initial package for fedora - no LTO
