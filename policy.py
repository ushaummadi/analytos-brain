ROLE_ACCESS = {

    "content-agent": [
        "Product",
        "Feature",
        "ProofPoint"
    ],

    "gtm-agent": [
        "Product",
        "Persona",
        "ICPSegment",
        "ProofPoint",
        "EmailThread"
    ]

}


def check_access(role, resource):

    return resource in ROLE_ACCESS.get(role, [])