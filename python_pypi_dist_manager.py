#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 Shlomi Fish <shlomif@cpan.org>
#
# Distributed under the terms of the MIT license.

from pydistman import DistManager


class Derived(DistManager):
    def _build_only_command_custom_steps(self):
        # self._dest_append("zenfilter/zenfilter.py", make_exe=True)
        for fn in ["{dest_dir}/setup.py", ]:
            self._re_mutate(
                fn_proto=fn,
                pattern="include_package_data=True,",
                repl_fn_proto=None,
                prefix="include_package_data=True,\n    " +
                "\n    entry_points={'console_scripts':[" +
                "'zenfilter=zenfilter:zenfilter',],},",
                )
        self._dest_append("MANIFEST.in")


dist_name = "zenfilter"

obj = Derived(
    dist_name=dist_name,
    dist_version="0.6.5",
    project_name="zenfilter",
    project_short_description="Filter stdin to avoid excessive output",
    release_date="2021-09-01",
    project_year="2016",
    aur_email="shlomif@cpan.org",
    project_email="shlomif@cpan.org",
    full_name="Shlomi Fish",
    github_username="shlomif",
)
obj.cli_run()
