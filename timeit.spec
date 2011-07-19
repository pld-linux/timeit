Summary:	TimeIt, the unobtrusive time tracker
Name:		timeit
Version:	0.9.7
Release:	0.1
License:	GPL v2
Group:		X11/Applications
Source0:	https://github.com/downloads/Hoglet/TimeIT/%{name}-%{version}.tar.gz
# Source0-md5:	60a400e271527dfcdc8d05fd8160fbe3
URL:		https://launchpad.net/timeit
BuildRequires:	boost-devel >= 1.33
BuildRequires:	gettext-devel
BuildRequires:	gtkmm-devel
BuildRequires:	intltool
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
TimeIT is a time tracker that works quietly almost without any
interaction and still measures the time you are spending on several
projects.

The concept of this program is that tasks and projects are assigned to
workspaces and while you are in those workspaces your projects are
timed.

It features workspace tracking, idle detection, editing of time
records and has summary views grouped by day, week, month, and year.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/%{name}.desktop
%{_datadir}/%{name}
%{_pixmapsdir}/%{name}.svg
