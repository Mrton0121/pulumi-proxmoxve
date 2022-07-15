// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.ProxmoxVE
{
    [ProxmoxVEResourceType("proxmoxve:index/certifi:Certifi")]
    public partial class Certifi : Pulumi.CustomResource
    {
        /// <summary>
        /// The PEM encoded certificate
        /// </summary>
        [Output("certificate")]
        public Output<string> Certificate { get; private set; } = null!;

        /// <summary>
        /// The PEM encoded certificate chain
        /// </summary>
        [Output("certificateChain")]
        public Output<string?> CertificateChain { get; private set; } = null!;

        /// <summary>
        /// The expiration date
        /// </summary>
        [Output("expirationDate")]
        public Output<string> ExpirationDate { get; private set; } = null!;

        /// <summary>
        /// The file name
        /// </summary>
        [Output("fileName")]
        public Output<string> FileName { get; private set; } = null!;

        /// <summary>
        /// The issuer
        /// </summary>
        [Output("issuer")]
        public Output<string> Issuer { get; private set; } = null!;

        /// <summary>
        /// The node name
        /// </summary>
        [Output("nodeName")]
        public Output<string> NodeName { get; private set; } = null!;

        /// <summary>
        /// Whether to overwrite an existing certificate
        /// </summary>
        [Output("overwrite")]
        public Output<bool?> Overwrite { get; private set; } = null!;

        /// <summary>
        /// The PEM encoded private key
        /// </summary>
        [Output("privateKey")]
        public Output<string> PrivateKey { get; private set; } = null!;

        /// <summary>
        /// The public key size
        /// </summary>
        [Output("publicKeySize")]
        public Output<int> PublicKeySize { get; private set; } = null!;

        /// <summary>
        /// The public key type
        /// </summary>
        [Output("publicKeyType")]
        public Output<string> PublicKeyType { get; private set; } = null!;

        /// <summary>
        /// The SSL fingerprint
        /// </summary>
        [Output("sslFingerprint")]
        public Output<string> SslFingerprint { get; private set; } = null!;

        /// <summary>
        /// The start date
        /// </summary>
        [Output("startDate")]
        public Output<string> StartDate { get; private set; } = null!;

        /// <summary>
        /// The subject
        /// </summary>
        [Output("subject")]
        public Output<string> Subject { get; private set; } = null!;

        /// <summary>
        /// The subject alternative names
        /// </summary>
        [Output("subjectAlternativeNames")]
        public Output<ImmutableArray<string>> SubjectAlternativeNames { get; private set; } = null!;


        /// <summary>
        /// Create a Certifi resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Certifi(string name, CertifiArgs args, CustomResourceOptions? options = null)
            : base("proxmoxve:index/certifi:Certifi", name, args ?? new CertifiArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Certifi(string name, Input<string> id, CertifiState? state = null, CustomResourceOptions? options = null)
            : base("proxmoxve:index/certifi:Certifi", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                PluginDownloadURL = "github://api.github.com/muhlba91/pulumi-proxmoxve",
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing Certifi resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Certifi Get(string name, Input<string> id, CertifiState? state = null, CustomResourceOptions? options = null)
        {
            return new Certifi(name, id, state, options);
        }
    }

    public sealed class CertifiArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The PEM encoded certificate
        /// </summary>
        [Input("certificate", required: true)]
        public Input<string> Certificate { get; set; } = null!;

        /// <summary>
        /// The PEM encoded certificate chain
        /// </summary>
        [Input("certificateChain")]
        public Input<string>? CertificateChain { get; set; }

        /// <summary>
        /// The node name
        /// </summary>
        [Input("nodeName", required: true)]
        public Input<string> NodeName { get; set; } = null!;

        /// <summary>
        /// Whether to overwrite an existing certificate
        /// </summary>
        [Input("overwrite")]
        public Input<bool>? Overwrite { get; set; }

        /// <summary>
        /// The PEM encoded private key
        /// </summary>
        [Input("privateKey", required: true)]
        public Input<string> PrivateKey { get; set; } = null!;

        public CertifiArgs()
        {
        }
    }

    public sealed class CertifiState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The PEM encoded certificate
        /// </summary>
        [Input("certificate")]
        public Input<string>? Certificate { get; set; }

        /// <summary>
        /// The PEM encoded certificate chain
        /// </summary>
        [Input("certificateChain")]
        public Input<string>? CertificateChain { get; set; }

        /// <summary>
        /// The expiration date
        /// </summary>
        [Input("expirationDate")]
        public Input<string>? ExpirationDate { get; set; }

        /// <summary>
        /// The file name
        /// </summary>
        [Input("fileName")]
        public Input<string>? FileName { get; set; }

        /// <summary>
        /// The issuer
        /// </summary>
        [Input("issuer")]
        public Input<string>? Issuer { get; set; }

        /// <summary>
        /// The node name
        /// </summary>
        [Input("nodeName")]
        public Input<string>? NodeName { get; set; }

        /// <summary>
        /// Whether to overwrite an existing certificate
        /// </summary>
        [Input("overwrite")]
        public Input<bool>? Overwrite { get; set; }

        /// <summary>
        /// The PEM encoded private key
        /// </summary>
        [Input("privateKey")]
        public Input<string>? PrivateKey { get; set; }

        /// <summary>
        /// The public key size
        /// </summary>
        [Input("publicKeySize")]
        public Input<int>? PublicKeySize { get; set; }

        /// <summary>
        /// The public key type
        /// </summary>
        [Input("publicKeyType")]
        public Input<string>? PublicKeyType { get; set; }

        /// <summary>
        /// The SSL fingerprint
        /// </summary>
        [Input("sslFingerprint")]
        public Input<string>? SslFingerprint { get; set; }

        /// <summary>
        /// The start date
        /// </summary>
        [Input("startDate")]
        public Input<string>? StartDate { get; set; }

        /// <summary>
        /// The subject
        /// </summary>
        [Input("subject")]
        public Input<string>? Subject { get; set; }

        [Input("subjectAlternativeNames")]
        private InputList<string>? _subjectAlternativeNames;

        /// <summary>
        /// The subject alternative names
        /// </summary>
        public InputList<string> SubjectAlternativeNames
        {
            get => _subjectAlternativeNames ?? (_subjectAlternativeNames = new InputList<string>());
            set => _subjectAlternativeNames = value;
        }

        public CertifiState()
        {
        }
    }
}
