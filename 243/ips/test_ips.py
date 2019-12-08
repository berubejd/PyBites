#!/usr/bin/env python3.8

import os
from pathlib import Path
from ipaddress import IPv4Network
from urllib.request import urlretrieve

import pytest

from ips import (ServiceIPRange, parse_ipv4_service_ranges,
                 get_aws_service_range)

URL = "https://bites-data.s3.us-east-2.amazonaws.com/ip-ranges.json"
TMP = os.getenv("TMP", "/tmp")
PATH = Path(TMP, "ip-ranges.json")
IP = IPv4Network('192.0.2.8/29')

@pytest.fixture(scope='module')
def json_file():
    """Import data into tmp folder"""
    urlretrieve(URL, PATH)
    return PATH


# write your pytest code ...
def test_dataclass():
    sipr = ServiceIPRange("TestService", "TestRegion", IP)
    assert str(sipr) == f"{IP} is allocated to the TestService service in the TestRegion region"

# Test parse_ipv4_services_ranges()?

def test_get_aws_service_range_address_error(json_file):
    service_ranges = parse_ipv4_service_ranges(json_file)

    with pytest.raises(ValueError) as excinfo:
        get_aws_service_range('7', service_ranges)
   
    assert "Address must be a valid IPv4 address" in str(excinfo.value)


def test_get_aws_service_range_success(json_file):
    service_ranges = parse_ipv4_service_ranges(json_file)

    sipr = get_aws_service_range('52.93.120.178', service_ranges)[0]
    assert sipr.service == 'AMAZON'
    assert sipr.region == 'us-west-1'
    assert str(sipr.cidr) == '52.93.120.178/32'
