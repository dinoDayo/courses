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
"""The command to enable Identity Service Feature."""

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from googlecloudsdk.calliope import base as calliope_base
from googlecloudsdk.command_lib.anthos.common import file_parsers
from googlecloudsdk.command_lib.container.fleet.features import base
from googlecloudsdk.command_lib.container.fleet.identity_service import utils

# Pull out the example text so the example command can be one line without the
# py linter complaining. The docgen tool properly breaks it into multiple lines.
EXAMPLES = """\
    To enable the Identity Service Feature, run:

    $ {command}
"""


class Enable(base.EnableCommand):
  """Enable Identity Service Feature.

  This command enables the Identity Service Feature in a fleet.
  """

  detailed_help = {'EXAMPLES': EXAMPLES}

  feature_name = 'identityservice'

  _fleet_default_member_config_supported_tracks = [
      calliope_base.ReleaseTrack.ALPHA, calliope_base.ReleaseTrack.BETA
  ]

  @classmethod
  def Args(cls, parser):
    if cls.ReleaseTrack(
    ) not in cls._fleet_default_member_config_supported_tracks:
      return

    parser.add_argument(
        '--fleet-default-member-config',
        type=str,
        hidden=True,
        help="""The path to an identity-service.yaml identity configuration file.
        This configuration would automatically get applied to every cluster that
        gets registered to the fleet and would act as the "source of truth" for
        such clusters. Any local authentication configuration found on any
        registered cluster would get overwritten by this configuration, including
        any local updates made after running this command with this flag.

        To enable the Identity Service with a default fleet level authentication configuration, run:

          $ {command} --fleet-default-member-config=/path/to/identity-service.yaml""",
    )

  def Run(self, args):
    empty_feature = self.messages.Feature()
    if self.ReleaseTrack(
    ) not in self._fleet_default_member_config_supported_tracks:
      return self.Enable(empty_feature)

    # run enable with an empty feature if the fleet_default_member_config
    # is not specified
    if not args.fleet_default_member_config:
      return self.Enable(empty_feature)

    # Load config YAML file.
    loaded_config = file_parsers.YamlConfigFile(
        file_path=args.fleet_default_member_config,
        item_type=file_parsers.LoginConfigObject)

    # Create new identity service feature spec.
    member_config = utils.parse_config(loaded_config, self.messages)

    # Create a feature object that has a default fleet identity service config
    feature = self.messages.Feature(
        fleetDefaultMemberConfig=self.messages
        .CommonFleetDefaultMemberConfigSpec(identityservice=member_config))

    return self.Enable(feature)
