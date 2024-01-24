%define _lto_cflags %{nil}

Name:           MusicSpectrum
Version:        0.0.5
Release:        8%{?dist}.nolto
Summary:        Audio spectrum viewer.

License:        CC0-1.0
URL:            https://github.com/geraldosimiao/MusicSpectrum.git
Source0:        https://github.com/geraldosimiao/MusicSpectrum/archive/refs/tags/%{version}.tar.gz
Patch:          ASSETS.patch

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
%autosetup -p1

%build
%cmake -DCMAKE_CXX_FLAGS="%{optflags} \
    -DMS_ASSETS_DIR='\"%{_datadir}/%{name}/assets\"'"
%cmake_build

%install
install -D -p -m755 \
    %{_builddir}/%{name}-%{version}/%{__cmake_builddir}/src/%{name} \
    %{buildroot}/%{_bindir}/%{name}
install -D -p -m644 LICENSES/CC0-1.0.txt \
    %{buildroot}/%{_datadir}/licenses/%{name}/CC0-1.0.txt
install -D -p -m644 README.md %{buildroot}/%{_docdir}/%{name}/README.md
mkdir -p %{buildroot}/%{_datadir}/%{name}
cp -a assets %{buildroot}/%{_datadir}/%{name}/

%files
%license CC0-1.0.txt
%doc README.md
%{_bindir}/%{name}
%{_datadir}/%{name}


%changelog
* Tue Jan 23 2024 Geraldo Simião <geraldosimiao@fedoraproject.org> - 0.0.5-8
- Initial package for fedora - no LTO
