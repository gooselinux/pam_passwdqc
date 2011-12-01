Summary: Pluggable password quality-control module
Name: pam_passwdqc
Version: 1.0.5
Release: 6%{?dist}
# License of man page is BSD, rest is Copyright only
License: BSD and Copyright only
Group: System Environment/Base
URL: http://www.openwall.com/passwdqc/
Source0: ftp://ftp.openwall.com/pub/projects/pam/modules/%name/%name-%version.tar.gz
Source1: ftp://ftp.openwall.com/pub/projects/pam/modules/%name/%name-%version.tar.gz.sign
BuildRequires: pam-devel
BuildRoot: %{_tmppath}/%name-%version

Patch1: patch-219201.patch 

%description
pam_passwdqc is a simple password strength checking module for
PAM-aware password changing programs, such as passwd(1).  In addition
to checking regular passwords, it offers support for passphrases and
can provide randomly generated passwords.  All features are optional
and can be (re-)configured without rebuilding.

%prep
%setup -q

%patch1 -p1

%build
make CFLAGS="-Wall -fPIC -DHAVE_SHADOW -DLINUX_PAM $RPM_OPT_FLAGS" LDFLAGS_LINUX='--shared -Wl,--version-script,$(MAP)'

%clean
rm -rf $RPM_BUILD_ROOT

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT MANDIR=%{_mandir} SECUREDIR=/%{_lib}/security

%files
%defattr(-,root,root)
%doc LICENSE README
/%{_lib}/security/pam_passwdqc.so
%{_mandir}/man*/*

%changelog
* Tue Apr 20 2010 Avesh Agarwal <avagarwa@redhat.com> - 1.0.5-6
- Added explanation of new options, disable_firstupper_lastdigit_check,
  oldpass_prompt_file, and newpass_prompt_file in the man pages
- Fixed output messages when disable_firstupper_lastdigit_check option
  is used 
Resolves: #219201 pam_passwdqc should be more configurable

* Wed Jan 13 2010 Avesh Agarwal <avagarwa@redhat.com> - 1.0.5-5
- Fixed following rpmlint errors on src rpm:
  pam_passwdqc.src: W: summary-ended-with-dot Pluggable
  password quality-control module.,
  pam_passwdqc.src:11: E: buildprereq-use pam-devel

* Tue Sep 29 2009 Avesh Agarwal <avagarwa@redhat.com> - 1.0.5-4
- Patch for new configurable options(rhbz# 219201): 
  disable first upper and last digit check, passwords 
  prompts can be read from a file
- Fixed an issue with spec file where "Release:" is not
  specified with "(?dist)". Without this, it gives problem
  when tagging across different fedora releases.  

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Jun  5 2008 Tomas Mraz <tmraz@redhat.com> - 1.0.5-1
- upgrade to a latest upstream version

* Wed Feb 20 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.0.4-5
- Autorebuild for GCC 4.3

* Wed Aug 22 2007 Tomas Mraz <tmraz@redhat.com> - 1.0.4-4
- clarify license even more

* Thu Aug 16 2007 Nalin Dahyabhai <nalin@redhat.com> - 1.0.4-3
- clarify license

* Sun Jul 29 2007 Nalin Dahyabhai <nalin@redhat.com> - 1.0.4-2
- set LDFLAGS_LINUX, not LDFLAGS, so that we don't strip the module before
  the debuginfo gets pulled out (#249963)

* Thu Jul 19 2007 Nalin Dahyabhai <nalin@redhat.com> - 1.0.4-1
- update to 1.0.4

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 1.0.2-1.2.2
- rebuild

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 1.0.2-1.2.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 1.0.2-1.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Fri Sep 16 2005 Nalin Dahyabhai <nalin@redhat.com> 1.0.2-1
- update to 1.0.2
- drop patch to use getpwnam_r() instead of getpwnam()

* Wed Mar 16 2005 Nalin Dahyabhai <nalin@redhat.com> 0.7.6-1
- update to 0.7.6, refines random= flag

* Mon Aug 16 2004 Nalin Dahyabhai <nalin@redhat.com> 0.7.5-2
- add %%clean stanza, pam-devel buildprereq

* Tue Apr 13 2004 Nalin Dahyabhai <nalin@redhat.com> 0.7.5-1
- bump release number to 1

* Tue Mar 30 2004 Nalin Dahyabhai <nalin@redhat.com> 0.7.5-0
- pull in Openwall package

* Fri Oct 31 2003 Solar Designer <solar@owl.openwall.com> 0.7.5-owl1
- Assume invocation by root only if both the UID is 0 and the PAM service
  name is "passwd"; this should solve changing expired passwords on Solaris
  and HP-UX and make "enforce=users" safe.
- Produce proper English explanations for a wider variety of settings.
- Moved the "-c" out of CFLAGS, renamed FAKEROOT to DESTDIR.

* Sat Jun 21 2003 Solar Designer <solar@owl.openwall.com> 0.7.4-owl1
- Documented that "enforce=users" may not always work for services other
  than the passwd command.
- Applied a patch to PLATFORMS from Mike Gerdts of GE Medical Systems
  to reflect how Solaris 8 patch 108993-18 (or 108994-18 on x86) changes
  Solaris 8's PAM implementation to look like Solaris 9.

* Mon Jun 02 2003 Solar Designer <solar@owl.openwall.com> 0.7.3.1-owl1
- Added URL.

* Thu Oct 31 2002 Solar Designer <solar@owl.openwall.com> 0.7.3-owl1
- When compiling with gcc, also link with gcc.
- Use $(MAKE) to invoke sub-makes.

* Fri Oct 04 2002 Solar Designer <solar@owl.openwall.com>
- Solaris 9 notes in PLATFORMS.

* Wed Sep 18 2002 Solar Designer <solar@owl.openwall.com>
- Build with Sun's C compiler cleanly, from Kevin Steves.
- Use install -c as that actually makes a difference on at least HP-UX
  (otherwise install would possibly move files and not change the owner).

* Fri Sep 13 2002 Solar Designer <solar@owl.openwall.com>
- Have the same pam_passwdqc binary work for both trusted and non-trusted
  HP-UX, from Kevin Steves.

* Fri Sep 06 2002 Solar Designer <solar@owl.openwall.com>
- Use bigcrypt() on HP-UX whenever necessary, from Kevin Steves of Atomic
  Gears LLC.
- Moved the old password checking into a separate function.

* Wed Jul 31 2002 Solar Designer <solar@owl.openwall.com>
- Call it 0.6.

* Sat Jul 27 2002 Solar Designer <solar@owl.openwall.com>
- Documented that the man page is under the 3-clause BSD-style license.
- HP-UX 11 support.

* Tue Jul 23 2002 Solar Designer <solar@owl.openwall.com>
- Applied minor corrections to the man page and at the same time eliminated
  unneeded/unimportant differences between it and the README.

* Sun Jul 21 2002 Solar Designer <solar@owl.openwall.com>
- 0.5.1: imported the pam_passwdqc(8) manual page back from FreeBSD.

* Tue Apr 16 2002 Solar Designer <solar@owl.openwall.com>
- 0.5: preliminary OpenPAM (FreeBSD-current) support in the code and related
code cleanups (thanks to Dag-Erling Smorgrav).

* Thu Feb 07 2002 Michail Litvak <mci@owl.openwall.com>
- Enforce our new spec file conventions.

* Sun Nov 04 2001 Solar Designer <solar@owl.openwall.com>
- Updated to 0.4:
- Added "ask_oldauthtok" and "check_oldauthtok" as needed for stacking with
the Solaris pam_unix;
- Permit for stacking of more than one instance of this module (no statics).

* Tue Feb 13 2001 Solar Designer <solar@owl.openwall.com>
- Install the module as mode 755.

* Tue Dec 19 2000 Solar Designer <solar@owl.openwall.com>
- Added "-Wall -fPIC" to the CFLAGS.

* Mon Oct 30 2000 Solar Designer <solar@owl.openwall.com>
- 0.3: portability fixes (this might build on non-Linux-PAM now).

* Fri Sep 22 2000 Solar Designer <solar@owl.openwall.com>
- 0.2: added "use_authtok", added README.

* Fri Aug 18 2000 Solar Designer <solar@owl.openwall.com>
- 0.1, "retry_wanted" bugfix.

* Sun Jul 02 2000 Solar Designer <solar@owl.openwall.com>
- Initial version (non-public).
