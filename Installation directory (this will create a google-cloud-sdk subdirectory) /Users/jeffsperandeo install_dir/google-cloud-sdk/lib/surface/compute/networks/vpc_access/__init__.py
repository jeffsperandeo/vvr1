# -*- coding: utf-8 -*- #
# Copyright 2018 Google LLC. All Rights Reserved.
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
"""The command group for the Cloud VPC Access Service."""

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from googlecloudsdk.calliope import base


# TODO(b/305707166): Change the marker if necessary when the bug is fixed.
@base.DefaultUniverseOnly
@base.ReleaseTracks(base.ReleaseTrack.GA, base.ReleaseTrack.BETA)
class VpcAccess(base.Group):
  """Manage VPC Access Service resources.

  Commands for managing Google VPC Access Service resources.
  """

  def Filter(self, context, args):
    del context, args
    # Explicitly enables user-project-override as it's disabled at compute
    # level.
    base.EnableUserProjectQuota()


@base.Hidden
@base.ReleaseTracks(base.ReleaseTrack.ALPHA)
class VpcAccessAlpha(base.Group):
  """Manage VPC Access Service resources.

  Commands for managing Google VPC Access Service resources.
  """

  def Filter(self, context, args):
    del context, args
    # Explicitly enables user-project-override as it's disabled at compute
    # level.
    base.EnableUserProjectQuota()
