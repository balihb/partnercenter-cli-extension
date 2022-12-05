# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long


def load_arguments(commands_loader, _):
    with commands_loader.argument_context('partnercenter marketplace offer listing uri') as c:
        c.argument('offer_id', options_list=['--offer-id'], help='The offer id.')
        c.argument('uri_type', options_list=['--type'], help='The type of the uri.')
        c.argument('subtype', options_list=['--subtype'], help='The subtype of the uri.')
        c.argument('display_text', options_list=['--display-text'], help='The display text of the uri.')
        c.argument('uri', options_list=['--uri'], help='The value of the uri.')
