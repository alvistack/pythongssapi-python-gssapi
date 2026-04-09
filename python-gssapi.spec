# Copyright 2026 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

%global source_date_epoch_from_changelog 0

Name: python-gssapi
Epoch: 100
Version: 1.11.1
Release: 1%{?dist}
Summary: Python GSSAPI Wrapper
License: ISC
URL: https://github.com/pythongssapi/python-gssapi/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: gcc
BuildRequires: krb5-devel >= 1.19
BuildRequires: python-rpm-macros
BuildRequires: python3-Cython3
BuildRequires: python3-devel
BuildRequires: python3-pip

%description
Python-GSSAPI provides both low-level and high level wrappers around the
GSSAPI C libraries. While it focuses on the Kerberos mechanism, it
should also be useable with other GSSAPI mechanisms.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
pip wheel \
    --no-deps \
    --no-build-isolation \
    --wheel-dir=dist \
    .

%install
pip install \
    --no-deps \
    --ignore-installed \
    --root=%{buildroot} \
    --prefix=%{_prefix} \
    dist/*.whl
find %{buildroot}%{python3_sitearch} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitearch}

%check

%if 0%{?suse_version} >= 1500
%package -n python%{python3_version_nodots}-gssapi
Summary: Python GSSAPI Wrapper
Requires: python3
Provides: python3-gssapi = %{epoch}:%{version}-%{release}
Provides: python3dist(gssapi) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-gssapi = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(gssapi) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-gssapi = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(gssapi) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-gssapi
Python-GSSAPI provides both low-level and high level wrappers around the
GSSAPI C libraries. While it focuses on the Kerberos mechanism, it
should also be useable with other GSSAPI mechanisms.

%files -n python%{python3_version_nodots}-gssapi
%license LICENSE.txt
%{python3_sitearch}/*
%endif

%if !(0%{?suse_version} >= 1500)
%package -n python3-gssapi
Summary: Python GSSAPI Wrapper
Requires: python3
Provides: python3-gssapi = %{epoch}:%{version}-%{release}
Provides: python3dist(gssapi) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-gssapi = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(gssapi) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-gssapi = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(gssapi) = %{epoch}:%{version}-%{release}

%description -n python3-gssapi
Python-GSSAPI provides both low-level and high level wrappers around the
GSSAPI C libraries. While it focuses on the Kerberos mechanism, it
should also be useable with other GSSAPI mechanisms.

%files -n python3-gssapi
%license LICENSE.txt
%{python3_sitearch}/*
%endif

%changelog
