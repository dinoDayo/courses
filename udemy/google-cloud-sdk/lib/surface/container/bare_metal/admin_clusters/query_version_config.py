# -*- coding: utf-8 -*- #
# Copyright 2022 Google LLC. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Command to query Anthos on bare metal admin cluster version configuration."""

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from googlecloudsdk.api_lib.container.gkeonprem import bare_metal_admin_clusters as apis
from googlecloudsdk.calliope import base
from googlecloudsdk.command_lib.container.bare_metal import cluster_flags as flags

_EXAMPLES = """
To query versions for creating an admin cluster, run:

$ {command}

To query versions for upgrading an admin cluster named `my-admin-cluster`,
run:

$ {command} --admin-cluster=my-admin-cluster
"""


@base.ReleaseTracks(base.ReleaseTrack.ALPHA)
class QueryVersionConfig(base.Command):
  """Query Anthos on bare metal admin cluster version configuration."""

  detailed_help = {'EXAMPLES': _EXAMPLES}

  @staticmethod
  def Args(parser):
    """Registers flags for this command."""
    flags.AddLocationResourceArg(parser, 'to query version configuration')
    flags.AddAdminConfigType(parser)

  def Run(self, args):
    """Runs the query-version-config command."""
    client = apis.AdminClustersClient()
    return client.QueryVersionConfig(args)
